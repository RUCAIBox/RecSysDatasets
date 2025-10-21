"""
一个全面的日志模块，提供彩色控制台输出和轮转文件日志功能.

该模块实现了单例模式的日志记录器，支持控制台和文件日志记录，
当日志文件达到10MB大小时会自动进行轮转.
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional, Union

from colorama import Fore, Style, init  # type: ignore

# 创建日志格式
LOG_FORMAT = "%(asctime)s [%(levelname)s] [%(module)s.%(funcName)s] - %(message)s"
# 包含 完整文件路径 和 行号
# LOG_FORMAT = "%(asctime)s [%(levelname)s] [%(pathname)s:%(lineno)d] - %(message)s"
# 包含 文件名 和 行号
# LOG_FORMAT = "%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s"

BERTOPIC_LOG_FORMAT = "%(asctime)s [%(levelname)s] [BERTopic] - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 初始化 colorama
init(autoreset=True)

# 定义日志级别对应的颜色
LOG_COLORS = {
    "DEBUG": Fore.CYAN,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.RED + Style.BRIGHT,
}

# 日志文件配置
MAX_LOG_SIZE = 10 * 1024 * 1024  # 10MB
BACKUP_COUNT = 5  # 保留5个备份文件


class ColoredFormatter(logging.Formatter):
    """自定义格式化器，为日志级别添加颜色."""

    def format(self, record):
        """格式化日志记录，为日志级别添加颜色."""
        # 获取原始日志消息
        message = super().format(record)

        # 为日志级别添加颜色
        level_color = LOG_COLORS.get(record.levelname, "")
        if level_color:
            # 只对日志级别关键字进行着色
            level_name = record.levelname
            colored_level = f"{level_color}{level_name}{Style.RESET_ALL}"
            message = message.replace(level_name, colored_level)

        return message


def setup_bertopic_logger(log_dir: Path):
    """
    配置 BERTopic 的日志记录器.

    Args:
        log_dir (Path): 日志目录路径
        bertopic_formatter (ColoredFormatter): BERTopic 专用的格式化器.
    """
    # 创建 BERTopic 专用格式化器
    bertopic_formatter = ColoredFormatter(BERTOPIC_LOG_FORMAT, datefmt=DATE_FORMAT)

    # 配置 BERTopic 的日志记录器
    bertopic_logger = logging.getLogger("BERTopic")
    bertopic_logger.setLevel(logging.INFO)
    bertopic_logger.propagate = False  # 禁止传播到根记录器

    # 移除现有的处理器（如果有的话）
    for handler in bertopic_logger.handlers[:]:
        bertopic_logger.removeHandler(handler)

    # 为 BERTopic 创建专用的处理器
    bertopic_console_handler = logging.StreamHandler(sys.stdout)
    bertopic_console_handler.setFormatter(bertopic_formatter)
    bertopic_logger.addHandler(bertopic_console_handler)

    # 使用轮转文件处理器
    bertopic_file_handler = RotatingFileHandler(
        log_dir / "pipeline.log",
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )
    bertopic_file_handler.setFormatter(bertopic_formatter)
    bertopic_logger.addHandler(bertopic_file_handler)


class Logger:
    """单例模式实现日志记录器."""

    _instance: Optional["Logger"] = None
    _initialized: bool = False

    def __new__(cls):
        """创建单例实例."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """初始化日志记录器."""
        if self._initialized:
            return

        self._initialized = True

        # 配置根日志记录器
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        # 移除所有现有的处理器
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

        # 创建日志目录
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        # 创建格式化器
        colored_formatter = ColoredFormatter(LOG_FORMAT, datefmt=DATE_FORMAT)
        plain_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

        # 控制台处理器（带颜色）
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(colored_formatter)
        root_logger.addHandler(console_handler)

        # 文件处理器（不带颜色，使用轮转）
        file_handler = RotatingFileHandler(
            log_dir / "pipeline.log",
            maxBytes=MAX_LOG_SIZE,
            backupCount=BACKUP_COUNT,
            encoding="utf-8",
        )
        file_handler.setFormatter(plain_formatter)
        root_logger.addHandler(file_handler)

        # 配置 BERTopic 的日志记录器
        setup_bertopic_logger(log_dir)

        # 创建项目特定的logger
        self.logger = logging.getLogger("TextMiningPipeline")
        self.logger.setLevel(logging.INFO)

        self.logger.propagate = True

    def get_logger(self) -> logging.Logger:
        """获取日志记录器实例."""
        return self.logger

    def set_level(self, level: int):
        """设置日志级别."""
        self.logger.setLevel(level)
        logging.getLogger().setLevel(level)


# Global logger instance
logger = Logger().get_logger()


def format_to_str_box(data: Union[dict[str, str], str], max_width: int = 80) -> str:
    """
    将字典或字符串格式化为指定格式的盒子字符串，自动处理长行.

    一个中文字符的宽度等于两个英文字符的宽度.

    参数:
        data: 可以是字典或字符串
              - 如果是字典：按key: value格式逐行显示
              - 如果是字符串：将字符串按行分割并显示在盒子中
        max_width: 每行最大显示宽度（不包括边框），默认80字符

    返回:
        格式化后的盒子字符串
    """
    # 计算字符的显示宽度
    def get_display_width(text):
        return sum(2 if "\u4e00" <= char <= "\u9fff" else 1 for char in text)

    def wrap_text(text: str, available_width: int) -> list[str]:
        """将长文本按指定宽度换行."""
        if get_display_width(text) <= available_width:
            return [text]

        words = text.split()
        lines = []
        current_line: list[str] = []
        current_width = 0

        for word in words:
            word_width = get_display_width(word)
            if (
                current_width + word_width + (1 if current_line else 0)
                <= available_width
            ):
                if current_line:
                    current_width += 1  # 空格的宽度
                current_line.append(word)
                current_width += word_width
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
                current_width = word_width

        if current_line:
            lines.append(" ".join(current_line))
        return lines

    result = ""
    border_length = max_width + 4  # 添加左右边距

    if isinstance(data, str):
        lines = []
        for line in data.split("\n"):
            lines.extend(wrap_text(line, max_width))

        # 创建顶部边框
        result = "+" + "-" * (border_length - 2) + "+\n"

        # 添加每一行内容
        for line in lines:
            display_width = get_display_width(line)
            padding = border_length - 4 - display_width  # -4 是因为"| "和" |"
            result += f"| {line}" + " " * padding + " |\n"

        # 添加底部边框
        result += "+" + "-" * (border_length - 2) + "+"

    elif isinstance(data, dict):
        # 创建顶部边框
        result = "+" + "-" * (border_length - 2) + "+\n"

        # 添加每一行内容
        for key, value in data.items():
            prefix = f"{key}: "
            prefix_width = get_display_width(prefix)
            available_width = max_width - prefix_width

            # 处理值的换行
            value_lines = wrap_text(str(value), available_width)

            # 添加第一行（带键名）
            first_line = prefix + value_lines[0]
            display_width = get_display_width(first_line)
            padding = border_length - 4 - display_width
            result += f"| {first_line}" + " " * padding + " |\n"

            # 添加后续行（如果有的话）
            for line in value_lines[1:]:
                display_width = get_display_width(line)
                # 对齐前一行的值
                indent = " " * prefix_width
                padding = border_length - 4 - display_width - prefix_width
                result += f"| {indent}{line}" + " " * padding + " |\n"

        # 添加底部边框
        result += "+" + "-" * (border_length - 2) + "+"

    else:
        raise TypeError("输入必须是字符串或字典")

    return "\n" + result

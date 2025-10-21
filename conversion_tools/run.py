# @Time   : 2020/9/18
# @Author : Shanlei Mu
# @Email  : slmu@ruc.edu.cn


import argparse
import importlib
import time
from datetime import datetime

from src.utils import dataset2class, click_dataset, multiple_dataset, multiple_item_features
from src.logger import logger, format_to_str_box


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='ml-1m')
    parser.add_argument('--input_path', type=str, default=None)
    parser.add_argument('--output_path', type=str, default=None)
    parser.add_argument('--interaction_type', type=str, default=None)
    parser.add_argument('--duplicate_removal', action='store_true')

    parser.add_argument('--item_feature_name', type=str, default='none')

    parser.add_argument('--convert_inter', action='store_true')
    parser.add_argument('--convert_item', action='store_true')
    parser.add_argument('--convert_user', action='store_true')

    args = parser.parse_args()

    assert args.input_path is not None, 'input_path can not be None, please specify the input_path'
    assert args.output_path is not None, 'output_path can not be None, please specify the output_path'

    # 构建配置信息
    config_info = {
        "数据集类型": args.dataset,
        "输入路径": args.input_path,
        "输出路径": args.output_path,
    }
    
    if args.interaction_type:
        config_info["交互类型"] = args.interaction_type
    
    config_info["去重模式"] = "已启用" if args.duplicate_removal else "未启用"
    config_info["开始时间"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 使用 logger 输出配置信息
    logger.info("=" * 80)
    logger.info("📊 数据集转换工具启动")
    logger.info(format_to_str_box(config_info))
    logger.info("=" * 80)

    start_time = time.time()

    input_args = [args.input_path, args.output_path]
    dataset_class_name = dataset2class[args.dataset.lower()]
    dataset_class = getattr(importlib.import_module('src.extended_dataset'), dataset_class_name)
    if dataset_class_name in multiple_dataset:
        # 只有当interaction_type不为None时才添加，否则传入'all'表示处理所有行为类型
        if args.interaction_type is not None:
            input_args.append(args.interaction_type)
        else:
            input_args.append('all')
    if dataset_class_name in click_dataset:
        input_args.append(args.duplicate_removal)
    if dataset_class_name in multiple_item_features:
        input_args.append(args.item_feature_name)
    
    logger.info(f"🔧 初始化数据集类: {dataset_class_name}")
    datasets = dataset_class(*input_args)
    logger.info("✅ 数据集类初始化完成")

    if args.convert_inter:
        logger.info("")
        logger.info("=" * 80)
        logger.info("🚀 开始转换交互数据 (Inter Data)")
        logger.info("=" * 80)
        datasets.convert_inter()
        logger.info("=" * 80)
        logger.info("✅ 交互数据转换完成")
        logger.info("=" * 80)
        
    if args.convert_item:
        logger.info("")
        logger.info("=" * 80)
        logger.info("🚀 开始转换物品特征 (Item Features)")
        logger.info("=" * 80)
        datasets.convert_item()
        logger.info("=" * 80)
        logger.info("✅ 物品特征转换完成")
        logger.info("=" * 80)

    if args.convert_user:
        logger.info("")
        logger.info("=" * 80)
        logger.info("🚀 开始转换用户特征 (User Features)")
        logger.info("=" * 80)
        datasets.convert_user()
        logger.info("=" * 80)
        logger.info("✅ 用户特征转换完成")
        logger.info("=" * 80)

    # 计算总耗时
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # 构建完成信息
    completion_info = {
        "状态": "所有任务完成",
        "总耗时": f"{elapsed_time:.2f} 秒 ({elapsed_time/60:.2f} 分钟)",
        "结束时间": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "输出目录": args.output_path
    }
    
    logger.info("")
    logger.info("=" * 80)
    logger.info("🎉 转换任务执行完毕")
    logger.info(format_to_str_box(completion_info))
    logger.info("=" * 80)

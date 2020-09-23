# Public Dataset 向 RecBox Dataset 的转换脚本

为了能将这些 public dataset 转换成 RecBox dataset 的格式，并将其应用到 RecBox 上，您只需要执行这两步：

## Step1
1) 根据本项目提供的各种数据集链接[数据集链接和简单介绍](),到对应位置下载你想要下载的数据集，下载完成后，对数据集进行解压。

2) 下载这些处理脚本
```
git clone https://github.com/RUCAIBox/RecommenderSystems-Datasets.git && cd RecommenderSystems-Datasets/Preprocessing
pip install -e . --verbose
```
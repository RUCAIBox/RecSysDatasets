# Public Dataset 向 RecBox Dataset 的转换脚本

为了能将这些 public dataset 转换成 RecBox dataset 的格式，并将其应用到 RecBox 上，您只需要执行这两步：

## Step1 下载原始数据集，并转换格式
1) 根据本项目提供的各种数据集链接[数据集链接和简单介绍](),到对应位置下载你想要下载的数据集，下载完成后，对数据集进行解压。

2) 下载这些处理脚本
```
git clone https://github.com/RUCAIBox/RecommenderSystems-Datasets.git
```

3) 进入到程序目录，执行相应程序，其中`input_path`为下载且解压后的数据集的目录位置, `output_path`为处理后数据的存储目录。

```
cd RecommenderSystems-Datasets/Preprocessing

python main.py --dataset [dataset_name] --input_path [input_path] --output_path [output_path]
```

## Step2 将其应用在RecBox中
1) 安装 RecBox， 请参考[link](https://github.com/RUCAIBox/RecBox)

2) 将从Step1获取的RecBox Dataset 移动到对应目录，就可以测试该数据集在RecBox中各个模型和各种评测方式下的表现了

3) 更多关于 RecBox 的使用，请参考[link]()
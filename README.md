# Datasets For Recommender Systems

This is a repository of public data sources for Recommender Systems (RS). 

## 数据集链接和简单介绍

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/): GroupLens Research has collected and made available rating datasets from their movie web site.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data): This is the official data set used in the Netflix Prize competition.

### Music
- [LastFM](https://grouplens.org/datasets/hetrec-2011/): This dataset contains social networking, tagging, and music artist listening information from a set of 2K users from Last.fm online music system.


## 数据集信息统计

常规数据集

   SN |Dataset|#User|#Item|#Inteaction|Sparsity|Interaction Type|TimeStamp|User Context| Item Context|Interaction Context|
|:---:|:----: |:---:|:---:|:--------:| :----: | :------------: |  :--------: |:--------: | :----------: | :---------------: |
| 1   |ML-1M  |6,040|3,952|1,000,209|95.81%  |Rating <br> [1-5]  |    √      |    √     |        √     |                   |



## 简单使用
如果想测试一下这些数据集在不同推荐系统模型下的表现，我们推荐你使用 [RecBox](https://github.com/RUCAIBox/RecBox)，一个集成了 
General, Context, Sequential, Knowledge 类模型的推荐系统库，模型涵盖范围广，使用便利。

如果想把上述介绍的数据集应用到RecBox中，您只需要简单两步操作就可以测试这些数据集在不同模型下的效果，首先您需要安装[RecBox](https://github.com/RUCAIBox/RecBox),
接着需要把原始的数据格式，转换成RecBox规定的数据格式，为此我们提供便捷的脚本，只需执行一下，即可转换完成，具体方式请参照 [Public dataset向RecBox dataset的转换]()。

如果您不想下载这些原始数据集，我们也把小部分经典的数据集处理好并共享出来了，您可以通过 [国内](), [国外]() 网盘连接进行获取。

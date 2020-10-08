# Datasets For Recommender Systems

This is a repository of public data sources for Recommender Systems (RS). 

## 数据集链接和简单介绍

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/): GroupLens Research has collected and made available rating datasets from their movie web site.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data): This is the official data set used in the Netflix Prize competition.

### Music
- [LastFM](https://grouplens.org/datasets/hetrec-2011/): This dataset contains social networking, tagging, and music artist listening information from a set of 2K users from Last.fm online music system.

### Anime
- [Anime](https://www.kaggle.com/CooperUnion/anime-recommendations-database): This dataset contains information on user preference data from myanimelist.net. Each user is able to add anime to their completed list and give it a rating and this data set is a compilation of those ratings.

### Shopping
- [Epinions](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data): This dataset was collected from Epinions.com, a popular online consumer review website.
- [Yelp](https://www.yelp.com/dataset): This dataset was collected from Yelp.com. The Yelp dataset is a subset of our businesses, reviews, and user data for use in personal, educational, and academic purposes.

### Advertisng

* [Criteo](https://www.kaggle.com/c/criteo-display-ad-challenge/data): This dataset was collected from Criteo, which consists of a portion of Criteo's traffic over a period of several days.

### Check-in

* [FourSquare](kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset): This dataset contains check-ins in NYC and Tokyo collected for about 10 month. Each check-in is associated with its time stamp, its GPS coordinates and its semantic meaning.




## 数据集信息统计

常规推荐数据集

   SN |Dataset|#User|#Item|#Inteaction|Sparsity|Interaction Type|TimeStamp|User Context| Item Context|Interaction Context| Reference (Paper/Competition/Website) |
|:---:|:----: |:---:|:---:|:--------:| :----: | :------------: |  :--------: |:--------: | :----------: | :---------------: |                                    |
| 1   |ML-1M  |6,040|3,952|1,000,209|95.81%  |Rating <br> [1-5]  |    √      |    √     |        √     |                   |                                     |
| 1   |Anime  |73,515|11,200|7,813,737|99.05%  |Rating <br> [-1, 1-10]  |          |         |        √     |                   |                                |
| 1   |Epinions  |116,260|41,269|188,478|99.99%  |Rating <br> [1-5]  |    √      |         |             |      √             |                                  |
| 1   |Yelp  |1,968,703|209,393|8,021,122|99.99%  |Rating <br> [1-5]  |    √      |    √   |      √      |      √             |                                  |
| 1   |FourSquare_NYC  |1,083|38,333|227,428|99.45%  |Click  |    √      |       |      √      |                   |                                             |
| 1   |FourSquare_TKY  |2,293|61,858|537,703|99.62%  |Click  |    √      |       |      √      |                   |                                             |

KG-aware推荐数据集




## 简单使用
如果想测试一下这些数据集在不同推荐系统模型下的表现，我们推荐你使用 [RecBox](https://github.com/RUCAIBox/RecBox)，一个集成了 
General, Context, Sequential, Knowledge 类模型的推荐系统库，模型涵盖范围广，使用便利。

如果想把上述介绍的数据集应用到RecBox中，您只需要简单两步操作就可以测试这些数据集在不同模型下的效果，首先您需要安装[RecBox](https://github.com/RUCAIBox/RecBox),
接着需要把原始的数据格式，转换成RecBox规定的数据格式。

针对如何获取RecBox规定的数据格式，我们提供两种处理方式：
1. 下载原始数据，使用便捷的脚本进行处理，具体方式请参照 [Public dataset向RecBox dataset的转换](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/Preprocessing)。

2. 直接下载已处理为RecBox格式的数据集（只包含部分数据集），您可以通过 [国内](), [国外]() 网盘连接进行获取。

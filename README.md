# Datasets For Recommender Systems

This is a repository of public data sources for Recommender Systems (RS). 

## 数据集链接和简单介绍

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/): GroupLens Research has collected and made available rating datasets from their movie web site.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data): This is the official data set used in the Netflix Prize competition.

### Music
- [LastFM](https://grouplens.org/datasets/hetrec-2011/): This dataset contains social networking, tagging, and music artist listening information from a set of 2K users from Last.fm online music system.
- [LFM-1b](http://www.cp.jku.at/datasets/LFM-1b/): This dataset contains more than one billion music listening events created by more than 120,000 users of Last.fm. Each listening event is characterized by artist, album, and track name, and includes a timestamp.
- 
### Anime
- [Anime](https://www.kaggle.com/CooperUnion/anime-recommendations-database): This dataset contains information on user preference data from myanimelist.net. Each user is able to add anime to their completed list and give it a rating and this data set is a compilation of those ratings.

### Shopping
- [Epinions](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data): This dataset was collected from Epinions.com, a popular online consumer review website.
- [Yelp](https://www.yelp.com/dataset): This dataset was collected from Yelp.com. The Yelp dataset is a subset of our businesses, reviews, and user data for use in personal, educational, and academic purposes.
- [Tmall](https://tianchi.aliyun.com/dataset/dataDetail?dataId=53): This dataset is provided by Ant Financial Services, using in the IJCAI16 contest.

### Advertisng

* [Criteo](https://www.kaggle.com/c/criteo-display-ad-challenge/data): This dataset was collected from Criteo, which consists of a portion of Criteo's traffic over a period of several days.
* [Avazu](https://www.kaggle.com/c/avazu-ctr-prediction/data): This dataset is used in avazu ctr prediction contest.

### Check-in

* [FourSquare](kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset): This dataset contains check-ins in NYC and Tokyo collected for about 10 month. Each check-in is associated with its time stamp, its GPS coordinates and its semantic meaning.
* [Gowalla](https://snap.stanford.edu/data/loc-gowalla.html): This dataset is from a location-based social networking website where users share their locations by checking-in, and contains a total of 6,442,890 check-ins of these users over the period of Feb. 2009 - Oct. 2010.

### Adult

* [Adult](http://archive.ics.uci.edu/ml/datasets/Adult): This dataset is extracted by Barry Becker from the 1994 Census database, which consists of a list of people's attributes and whether they make over 50k a year.




## 数据集信息统计

常规推荐数据集


| SN | Dataset         | \#User    | \#Item    | \#Inteaction | Sparsity | Interaction Type                    | TimeStamp | User Context | Item Context | Interaction Context | Reference \(Paper/Competition/Website\)       |
|----|-----------------|-----------|-----------|--------------|----------|-------------------------------------|-----------|--------------|--------------|---------------------|-----------------------------------------------|
| 1  | ml\-100k        | 943       | 1,682     | 100,000      | 93\.70%  | Rating <br> \[1\-5\]                | √         | √            | √            |                     | The MovieLens Datasets: History and Context\. |
| 2  | ml\-1m          | 6,040     | 3,952     | 1,000,209    | 95\.81%  | Rating <br> \[1\-5\]                | √         | √            | √            |                     | The MovieLens Datasets: History and Context\. |
| 3  | ml\-10m         | 69,878    | 10,681    | 10,000,054   | 98\.69%  | Rating <br> \[0\.5\-5\] half\-stars | √         |              | √            |                     | The MovieLens Datasets: History and Context\. |
| 4  | ml\-20m         | 138,493   | 27,278    | 20,000,263   | 99\.47   | Rating <br> \[0\.5\-5\] half\-stars | √         |              | √            |                     | The MovieLens Datasets: History and Context\. |
| 5  | Anime           | 73,515    | 11,200    | 7,813,737    | 99\.05%  | Rating <br> \[\-1, 1\-10\]          |           |              | √            |                     |                                               |
| 6  | Epinions        | 116,260   | 41,269    | 188,478      | 99\.99%  | Rating <br> \[1\-5\]                | √         |              |              | √                   |                                               |
| 7  | Yelp            | 1,968,703 | 209,393   | 8,021,122    | 99\.99%  | Rating <br> \[1\-5\]                | √         | √            | √            | √                   |                                               |
| 8  | FourSquare\_NYC | 1,083     | 38,333    | 227,428      | 99\.45%  | Click                               | √         |              | √            |                     |                                               |
| 9  | FourSquare\_TKY | 2,293     | 61,858    | 537,703      | 99\.62%  | Click                               | √         |              | √            |                     |                                               |
| 10 | Avazu           |           |           | 40,428,967   |          | Click <br> \[0, 1\]                 | √         |              |              | √                   |                                               |
| 11 | Netflix         | 480,190   | 17,771    | 100,480,507  | 98\.99%  | Rating <br> \[1\-5\]                | √         |              |              |                     |                                               |
| 12 | Tmall           | 963,924   | 2,353,208 | 31,955,771   | 99\.99%  | Click or Buy <br> \[0, 1\]          | √         |              |              | √                   |                                               |
| 13 | Adult           |           |           | 32,561       |          | income>=50k <br> \[0, 1\]           |           |              |              |                     |                                               |
| 14 | Gowalla         |107,092    | 1,280,969  | 3,981,334   | 99\.99%  | Click                               | √         |              |              | √                  |                                               |
| 15 | LastFM          |1,892      | 17,632    | 92,834       | 99\.72%  | Click                               |           |              |              | √                  |                                               |
| 16 | lfm1b-artists   |120,322    | 3,123,496  | 65,133,026  | 99\.98%  | Click                               | √         | √            | √            | √                  |                                               |
| 17 | lfm1b-albums    |120,322    | 15,641,432  | 117,997,821  | 99\.99%  | Click                             | √         | √            | √            | √                  |    
| 18 | lfm1b-tracks    |120,322    | 31,634,450  | 319,951,294  | 99\.99%  | Click                             | √         | √            | √            | √                  |                                              |


KG-aware推荐数据集




## 简单使用
如果想测试一下这些数据集在不同推荐系统模型下的表现，我们推荐你使用 [RecBox](https://github.com/RUCAIBox/RecBox)，一个集成了 
General, Context, Sequential, Knowledge 类模型的推荐系统库，模型涵盖范围广，使用便利。

如果想把上述介绍的数据集应用到RecBox中，您只需要简单两步操作就可以测试这些数据集在不同模型下的效果，首先您需要安装[RecBox](https://github.com/RUCAIBox/RecBox),
接着需要把原始的数据格式，转换成RecBox规定的数据格式。

针对如何获取RecBox规定的数据格式，我们提供两种处理方式：
1. 下载原始数据，使用便捷的脚本进行处理，具体方式请参照 [Public dataset向RecBox dataset的转换](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/Preprocessing)。

2. 直接下载已处理为RecBox格式的数据集（只包含部分数据集），您可以通过 [国内](), [国外]() 网盘连接进行获取。

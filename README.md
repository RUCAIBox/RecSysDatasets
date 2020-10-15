# Datasets For Recommender Systems

This is a repository of public data sources for Recommender Systems (RS). 

## 数据集链接和简单介绍

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/): GroupLens Research has collected and made available rating datasets from their movie web site.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data): This is the official data set used in the Netflix Prize competition.

### Music
- [LastFM](https://grouplens.org/datasets/hetrec-2011/): This dataset contains social networking, tagging, and music artist listening information from a set of 2K users from Last.fm online music system.
- [LFM-1b](http://www.cp.jku.at/datasets/LFM-1b/): This dataset contains more than one billion music listening events created by more than 120,000 users of Last.fm. Each listening event is characterized by artist, album, and track name, and includes a timestamp.
- [Yahoo Music](https://webscope.sandbox.yahoo.com/catalog.php?datatype=r): This dataset represents a snapshot of the Yahoo! Music community's preferences for various musical artists.
### Anime
- [Anime](https://www.kaggle.com/CooperUnion/anime-recommendations-database): This dataset contains information on user preference data from myanimelist.net. Each user is able to add anime to their completed list and give it a rating and this data set is a compilation of those ratings.

### Shopping
- [Epinions](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data): This dataset was collected from Epinions.com, a popular online consumer review website.
- [Yelp](https://www.yelp.com/dataset): This dataset was collected from Yelp.com. The Yelp dataset is a subset of our businesses, reviews, and user data for use in personal, educational, and academic purposes.
- [Tmall](https://tianchi.aliyun.com/dataset/dataDetail?dataId=53): This dataset is provided by Ant Financial Services, using in the IJCAI16 contest.
- [DIGINETICA](https://competitions.codalab.org/competitions/11161):The dataset includes user sessions extracted from an e-commerce search engine logs, with anonymized user ids, hashed queries, hashed query terms, hashed product descriptions and meta-data, log-scaled prices, clicks, and purchases.
- [YOOCHOOSE](https://2015.recsyschallenge.com/challenge.html): This dataset was constructed by YOOCHOOSE GmbH to support participants in the RecSys Challenge 2015.
- [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset): The data has been collected from a real-world ecommerce website. It is raw data, i.e. without any content transformations, however, all values are hashed due to confidential issues.

### Advertisng

* [Criteo](https://www.kaggle.com/c/criteo-display-ad-challenge/data): This dataset was collected from Criteo, which consists of a portion of Criteo's traffic over a period of several days.
* [Avazu](https://www.kaggle.com/c/avazu-ctr-prediction/data): This dataset is used in avazu ctr prediction contest.
* [Ipinyou](https://pan.baidu.com/s/1kTwX2mF#list/path=%2F): This dataset was provided by iPinYou, which contains all training datasets and leaderboard testing datasets of the three seasons iPinYou Global RTB(Real-Time Bidding) Bidding Algorithm Competition.

### Check-in

* [FourSquare](kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset): This dataset contains check-ins in NYC and Tokyo collected for about 10 month. Each check-in is associated with its time stamp, its GPS coordinates and its semantic meaning.
* [Gowalla](https://snap.stanford.edu/data/loc-gowalla.html): This dataset is from a location-based social networking website where users share their locations by checking-in, and contains a total of 6,442,890 check-ins of these users over the period of Feb. 2009 - Oct. 2010.

### Adult

* [Adult](http://archive.ics.uci.edu/ml/datasets/Adult): This dataset is extracted by Barry Becker from the 1994 Census database, which consists of a list of people's attributes and whether they make over 50k a year.

### Game

* [Steam](http://cseweb.ucsd.edu/~wckang/steam_reviews.json.gz): This dataset is reviews and game information from Steam, which contains 7,793,069 reviews, 2,567,538 users, and 32,135 games. In addition to the review text, the data also includes the users' play hours in each review.

### Pinterest

* [pinterest](https://github.com/hexiangnan/neural_collaborative_filtering/tree/master/Data): This dataset is originally constructed by paper Learning image and user features for recommendations in social networks for evaluating content-based image recommendation, and processed by paper Neural Collaborative Filtering.

### Website

* [Phishing-website](http://archive.ics.uci.edu/ml/datasets/Phishing+Websites): This dataset contains 30 features of 11,055 websites and labels of whether they are phishing websites or not. The websites' features includes 12 address-bar based features, 6 abnormal based features, 5 HTML-and-JavaScript based features and 7 domain based features.



## 数据集信息统计

常规推荐数据集


| SN | Dataset         | \#User    | \#Item    | \#Inteaction | Sparsity | Interaction Type                    | TimeStamp | User Context | Item Context | Interaction Context | Reference \(Paper/Competition/Website\)       |
|----|-----------------|-----------|-----------|--------------|----------|-------------------------------------|-----------|--------------|--------------|---------------------|-----------------------------------------------|
| 1  | ml\-100k        | 943       | 1,682     | 100,000      | 93\.70%  | Rating <br> \[1\-5\]                | √         | √            | √            |                     | The MovieLens Datasets: History and Context\. |
| 2  | ml\-1m          | 6,040     | 3,952     | 1,000,209    | 95\.81%  | Rating <br> \[1\-5\]                | √         | √            | √            |                     | The MovieLens Datasets: History and Context\. |
| 3  | ml\-10m         | 69,878    | 10,681    | 10,000,054   | 98\.69%  | Rating <br> \[0\.5\-5\] half\-stars | √         |              | √            |                     | The MovieLens Datasets: History and Context\. |
| 4  | ml\-20m         | 138,493   | 27,278    | 20,000,263   | 99\.47   | Rating <br> \[0\.5\-5\] half\-stars | √         |              | √            |                     | The MovieLens Datasets: History and Context\. |
| 5  | Anime           | 73,515    | 11,200    | 7,813,737    | 99\.05%  | Rating <br> \[\-1, 1\-10\]          |           |              | √            |                     | Kaggle: https://www.kaggle.com/CooperUnion/anime-recommendations-database |
| 6  | Epinions        | 116,260   | 41,269    | 188,478      | 99\.99%  | Rating <br> \[1\-5\]                | √         |              |              | √        | Leveraging Social Connections to Improve Personalized Ranking for Collaborative Filtering.|
| 7  | Yelp            | 1,968,703 | 209,393   | 8,021,122    | 99\.99%  | Rating <br> \[1\-5\]                | √         | √            | √            | √                   | Yelp Dataset: https://www.yelp.com/dataset |
| 8  | FourSquare\_NYC | 1,083     | 38,333    | 227,428      | 99\.45%  | Click                               | √         |              | √            |                     | Kaggle: https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset |
| 9  | FourSquare\_TKY | 2,293     | 61,858    | 537,703      | 99\.62%  | Click                               | √         |              | √            |                     | Kaggle: https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset |
| 10 | Avazu           |           |           | 40,428,967   |          | Click <br> \[0, 1\]                 | √         |              |              | √                   | Kaggle: https://www.kaggle.com/c/avazu-ctr-prediction/data |
| 11 | Netflix         | 480,189 | 17,770   | 100,480,507  | 98\.82% | Rating <br> \[1\-5\]                | √         |              |              |                     | Kaggle: https://www.kaggle.com/netflix-inc/netflix-prize-data |
| 12 | Tmall-Buy       | 885,759 | 1,144,124 | 9,348,756 | 99\.99%  | Buy          | √         |              |              |                    | IJCAI16 Contest: https://tianchi.aliyun.com/dataset/dataDetail?dataId=53 |
| 13 | Tmall-Click     | 626,041 | 2,200,291 | 35,179,371 | 99\.99%  | Click         | √         |              |              |                    | IJCAI16 Contest: https://tianchi.aliyun.com/dataset/dataDetail?dataId=53 |
| 14 | Tmall-Buy-Sums  | 885,759 | 1,144,124 | 7,592,214 | 99\.99%  | Buy         | √         |              |              | √                   | IJCAI16 Contest: https://tianchi.aliyun.com/dataset/dataDetail?dataId=53 |
| 15 | Tmall-Click-Sums | 626,041 | 2,200,291 | 24,363,557 | 99\.99%  | Click          | √         |              |              | √                   | IJCAI16 Contest: https://tianchi.aliyun.com/dataset/dataDetail?dataId=53 |
| 16 | Adult           |           |           | 32,561       |          | income>=50k <br> \[0, 1\]           |           |              |              | √ | Adult Dataset: http://archive.ics.uci.edu/ml/datasets/Adult |
| 17 | Gowalla         |107,092    | 1,280,969  | 3,981,334   | 99\.99%  | Click                               | √         |              |              | √                  |                                               |
| 18  | LastFM          | 1,892     | 17,632    | 92,834       | 99\.72%  | Click                               |           |              |              | √                   | HetRec 2011 Dataset: https://grouplens.org/datasets/hetrec-2011/ |
| 19  | DIGINETICA      | 600,684   | 184,047   | 993,483      | 99.99%   | Click                               | √         |              | √            |                     | CIKM Cup 2016 Track 2: Personalized E-Commerce Search Challenge<br>https://competitions.codalab.org/competitions/11161 |
| 20 | lfm1b-artists   |120,322    | 3,123,496  | 65,133,026  | 99\.98%  | Click                               | √         | √            | √            | √                  |                                               |
| 21 | lfm1b-albums    |120,322    | 15,641,432  | 117,997,821  | 99\.99%  | Click                             | √         | √            | √            | √                  ||
| 22 | lfm1b-tracks    |120,322    | 31,634,450  | 319,951,294  | 99\.99%  | Click                             | √         | √            | √            | √                  |                                              |
| 23 | criteo | |  | 45,850,617 |  | Click |  |  |  | √ | |
| 24 | Book-crossing | 105284 | 340557 | 1149780 | 99.99% | Rating<br>[0-10] | | √ | √ |  | Improving Recommendation Lists Through Topic Diversification |
| 25 | steam | 2,567,538 | 32,135 | 7,793,069 | 99\.99% | Buy | √ |  | √ | √ | Self-Attentive Sequential Recommendation. |
| 26 | Yahoo Music | 1,948,882 | 98,211 | 11,557,943 | 99.99% | Rating<br>[0, 100] |  | | √ |  | Yahoo Rating and Classification Data: https://webscope.sandbox.yahoo.com/catalog.php?datatype=r |
| 27 | YOOCHOOSE-Buys |  |  | 1,150,753 |  | Click | √ | |  | √ | RecSys Challenge 2015: https://2015.recsyschallenge.com/challenge.html |
| 28 | YOOCHOOSE-Clicks |  |  | 33,003,944 |  | Click | √ | |  | √ | RecSys Challenge 2015: https://2015.recsyschallenge.com/challenge.html |
| 29 | Pinterest | 55,187 | 9,911 | 1,445,622 | 99.74% |  |  | |  |  | Neural Collaborative Filtering |
| 30 | IPinyou-View | 12,930,288 | 131 | 15,354,629 | 99.09% | View |  | √ | √ | √ | iPinYou Global RTB Bidding Algorithm Competition: http://contest.ipinyou.com |
| 31 | IPinyou-Click | 11,597 | 118 | 12,683 | 99.07% | Click |  | √ | √ | √ | iPinYou Global RTB Bidding Algorithm Competition: http://contest.ipinyou.com |
| 32 | IPinyou-View-Sums | 12,930,288 | 131 | 14,697,046 | 99.13% | View |  | √ | √ | √ | iPinYou Global RTB Bidding Algorithm Competition: http://contest.ipinyou.com |
| 33 | IPinyou-Click-Sums | 11,597 | 118 | 11,615 | 99.15% | Click |  | √ | √ | √ | iPinYou Global RTB Bidding Algorithm Competition: http://contest.ipinyou.com |
| 34 | Phishing-website |  |  | 11,055 |  |  |  | |  | √ | An Assessment of Features Related to Phishing Websites using an Automated Technique. |
| 35 | Retailrocket-View | | | 2,664,312 | | Click | √ | | |  | Kaggle: https://www.kaggle.com/retailrocket/ecommerce-dataset |
| 36 | Retailrocket-Addtocart | | | 69,332 | | Click | √ | | |  | Kaggle: https://www.kaggle.com/retailrocket/ecommerce-dataset |
| 37 | Retailrocket-Transaction | | | 22,457 | | Click | √ | | |  | Kaggle: https://www.kaggle.com/retailrocket/ecommerce-dataset |


KG-aware推荐数据集




## 简单使用
如果想测试一下这些数据集在不同推荐系统模型下的表现，我们推荐你使用 [RecBox](https://github.com/RUCAIBox/RecBox)，一个集成了 
General, Context, Sequential, Knowledge 类模型的推荐系统库，模型涵盖范围广，使用便利。

如果想把上述介绍的数据集应用到RecBox中，您只需要简单两步操作就可以测试这些数据集在不同模型下的效果，首先您需要安装[RecBox](https://github.com/RUCAIBox/RecBox),
接着需要把原始的数据格式，转换成RecBox规定的数据格式。

针对如何获取RecBox规定的数据格式，我们提供两种处理方式：
1. 下载原始数据，使用便捷的脚本进行处理，具体方式请参照 [Public dataset向RecBox dataset的转换](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/Preprocessing)。

2. 直接下载已处理为RecBox格式的数据集（只包含部分数据集），您可以通过 [国内](), [国外]() 网盘连接进行获取。

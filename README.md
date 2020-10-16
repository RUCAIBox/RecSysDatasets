# Datasets For Recommender Systems

This is a repository of public data sources for Recommender Systems (RS). 

## 数据集链接和简单介绍

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/): GroupLens Research has collected and made available rating datasets from their movie web site.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data): This is the official data set used in the Netflix Prize competition.
- [Douban](https://www.kaggle.com/utmhikari/doubanmovieshortcomments):  Douban Movie is a Chinese website that allows Internet users to share their comments and viewpoints about movies. This dataset contains more than 2 million short comments of 28 movies in Douban Movie website. 

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

- [Ta Feng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset): The dataset contains a Chinese grocery store transaction data from November 2000 to February 2001.

- [Amazon](http://jmcauley.ucsd.edu/data/amazon/): This dataset contains product reviews and metadata from Amazon, including 142.8 million reviews spanning May 1996 - July 2014.

  This dataset includes only-rating data (ratings), product metadata (descriptions, category information, price, brand, and image features), and links (also viewed/also bought graphs).

### Advertisng

* [Criteo](https://www.kaggle.com/c/criteo-display-ad-challenge/data): This dataset was collected from Criteo, which consists of a portion of Criteo's traffic over a period of several days.
* [Avazu](https://www.kaggle.com/c/avazu-ctr-prediction/data): This dataset is used in avazu ctr prediction contest.
* [Ipinyou](http://contest.ipinyou.com): This dataset was provided by iPinYou, which contains all training datasets and leaderboard testing datasets of the three seasons iPinYou Global RTB(Real-Time Bidding) Bidding Algorithm Competition.

### Check-in

* [FourSquare](kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset): This dataset contains check-ins in NYC and Tokyo collected for about 10 month. Each check-in is associated with its time stamp, its GPS coordinates and its semantic meaning.
* [Gowalla](https://snap.stanford.edu/data/loc-gowalla.html): This dataset is from a location-based social networking website where users share their locations by checking-in, and contains a total of 6,442,890 check-ins of these users over the period of Feb. 2009 - Oct. 2010.

### Adult

* [Adult](http://archive.ics.uci.edu/ml/datasets/Adult): This dataset is extracted by Barry Becker from the 1994 Census database, which consists of a list of people's attributes and whether they make over 50k a year.

### Games

* [Steam](https://github.com/kang205/SASRec): This dataset is reviews and game information from Steam, which contains 7,793,069 reviews, 2,567,538 users, and 32,135 games. In addition to the review text, the data also includes the users' play hours in each review.

### Pinterest

* [Pinterest](https://github.com/hexiangnan/neural_collaborative_filtering/tree/master/Data): This dataset is originally constructed by paper Learning image and user features for recommendations in social networks for evaluating content-based image recommendation, and processed by paper Neural Collaborative Filtering.

### Websites

* [Phishing-website](http://archive.ics.uci.edu/ml/datasets/Phishing+Websites): This dataset contains 30 features of 11,055 websites and labels of whether they are phishing websites or not. The websites' features includes 12 address-bar based features, 6 abnormal based features, 5 HTML-and-JavaScript based features and 7 domain based features.

### Jokes

* [Jester](http://eigentaste.berkeley.edu/dataset/): This dataset contains anonymous ratings of jokes by users of the Jester Joke Recommender System.

### Books

* [Book-Crossing](http://www2.informatik.uni-freiburg.de/~cziegler/BX/): This dataset was collected by Cai-Nicolas Ziegler in a 4-week crawl (August / September 2004) from the [Book-Crossing](http://www.bookcrossing.com/) community with kind permission from Ron Hornbaker, CTO of [Humankind Systems](http://www.humankindsystems.com/). Contains 278,858 users (anonymized but with demographic information) providing 1,149,780 ratings (explicit / implicit) about 271,379 books.

### Exercises

* [KDD2010-bridge](https://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp): This dataset was released in KDD Cup 2010 Educational Data Mining Challenge,  which contains the situations of students submitting exercises on the systems.


## 数据集信息统计

常规推荐数据集


| SN | Dataset           | \#User    | \#Item    | \#Inteaction | Sparsity | Interaction Type           | TimeStamp | User Context | Item Context | Interaction Context |
|----|-------------------|-----------|-----------|--------------|----------|----------------------------|-----------|--------------|--------------|---------------------|
| 1  | [MovieLens](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/MovieLens)         | \-        | \-        | \-           | \-       | Rating                     | √         | √            | √            |                     |
| 2  | Anime             | 73,515    | 11,200    | 7,813,737    | 99\.05%  | Rating <br> \[\-1, 1\-10\] |           |              | √            |                     |
| 3  | Epinions          | 116,260   | 41,269    | 188,478      | 99\.99%  | Rating <br> \[1\-5\]       | √         |              |              | √                   |
| 4  | Yelp              | 1,968,703 | 209,393   | 8,021,122    | 99\.99%  | Rating <br> \[1\-5\]       | √         | √            | √            | √                   |
| 5  | Netflix           | 480,189   | 17,770    | 100,480,507  | 98\.82%  | Rating <br> \[1\-5\]       | √         |              |              |                     |
| 6  | Book\-crossing    | 105,284   | 340,557   | 1,149,780    | 99\.99%  | Rating <br> \[0\-10\]      |           | √            | √            |                     |
| 7  | Jester            | 73,421    | 101       | 4,136,360    | 44\.22%  | Rating <br> \[\-10, 10\]   |           |              |              |                     |
| 8  | Douban            | 738,701   | 28        | 2,125,056    | 89\.73%  | Rating <br> \[0,5\]        | √         |              |              | √                   |
| 9  | Yahoo Music       | 1,948,882 | 98,211    | 11,557,943   | 99\.99%  | Rating <br> \[0, 100\]     |           |              | √            |                     |
| 10 | [KDD2010](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/KDD2010)           | \-        | \-        | \-           | \-       | Rating                     |           |              |              | √                   |
| 11 | [Amazon](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Amazon)            | \-        | \-        | \-           | \-       | Rating                     | √         |              | √            |                     |
| 12 | Pinterest         | 55,187    | 9,911     | 1,445,622    | 99\.74%  | \-                         |           |              |              |                     |
| 13 | [Gowalla](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Gowalla)           | 107,092   | 1,280,969 | 6,442,892   | 99\.99%  | Check-in                   | √         |              |              | √                   |
| 14 | LastFM            | 1,892     | 17,632    | 92,834       | 99\.72%  | Click                      |           |              |              | √                   |
| 15 | [DIGINETICA](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/DIGINETICA)        | 600,684   | 184,047   | 993,483      | 99\.99%  | Click                      | √         |              | √            |                     |
| 16 | [Steam](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Steam)             | 2,567,538 | 32,135    | 7,793,069    | 99\.99%  | Buy                        | √         |              | √            | √                   |
| 17 | [Ta Feng](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/TaFeng)           | 32,266    | 23,812    | 817,741      | 99\.89%  | Click                      | √         | √            | √            | √                   |
| 18 | [FourSquare](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/FourSquare)        | \-        | \-        | \-           | \-       | Check-in                   | √         |              | √            |                     |
| 19 | [Tmall](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Tmall)             | 963,923 | 2,353,207 | 44,528,127 | 99.99% | Click/Buy                  | √         |              |              | √                   |
| 20 | [YOOCHOOSE](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/YOOCHOOSE)         | \-        | \-        | \-           | \-       | Click/Buy                  | √         |              |              | √                   |
| 21 | [IPinyou](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/IPinyou)           | 12,931,430 | 131 | 15,367,312 | 99.09% | View/Click                 |           | √            | √            | √                   |
| 22 | [Retailrocket](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Retailrocket)      | \-        | \-        | \-           | \-       | View/Addtocart/Transaction | √         |              |              |                     |
| 23 | [LFM-1b](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/LFM-1b)            | 120,322   | 3,123,496 | 1,088,161,692   | 99\.71%  | Click                      | √         | √            | √            | √                   |
| 24 | Criteo            | \-        | \-        | 45,850,617   | \-       | Click                      |           |              |              | √                   |
| 25 | Avazu             | \-        | \-        | 40,428,967   | \-       | Click <br> \[0, 1\]        | √         |              |              | √                   |
| 26 | Phishing\-website | \-        | \-        | 11,055       | \-       |                            |           |              |              | √                   |
| 27 | Adult             | \-        | \-        | 32,561       | \-       | income>=50k <br> \[0, 1\]  |           |              |              | √                   |


KG-aware推荐数据集




## 简单使用
如果想测试一下这些数据集在不同推荐系统模型下的表现，我们推荐你使用 [RecBox](https://github.com/RUCAIBox/RecBox)，一个集成了 
General, Context, Sequential, Knowledge 类模型的推荐系统库，模型涵盖范围广，使用便利。

如果想把上述介绍的数据集应用到RecBox中，您只需要简单两步操作就可以测试这些数据集在不同模型下的效果，首先您需要安装[RecBox](https://github.com/RUCAIBox/RecBox),
接着需要把原始的数据格式，转换成RecBox规定的数据格式。

针对如何获取RecBox规定的数据格式，我们提供两种处理方式：
1. 下载原始数据，使用便捷的脚本进行处理，具体方式请参照 [Public dataset向RecBox dataset的转换](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/Preprocessing)。

2. 直接下载已处理为RecBox格式的数据集（只包含部分数据集），您可以通过 [国内](), [国外]() 网盘连接进行获取。

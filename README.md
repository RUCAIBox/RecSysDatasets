# Datasets For Recommender Systems

This is a repository of public data sources for Recommender Systems (RS).

All of these recommendation datasets can convert to the atomic files
defined in [RecBole](https://github.com/RUCAIBox/RecBole),
which is a unified, comprehensive and efficient recommendation library.

After converting to the atomic files, you can use RecBole
to test the performance of different recommender models on these datasets easily.
For more information about RecBole, please refer to [RecBole](https://github.com/RUCAIBox/RecBole).


## Usage
In order to use RecBole, you need to convert these original datasets to the atomic file
which is a kind of data format defined by RecBole.

We provide two ways to convert these datasets into atomic files:

1. Download the raw dataset and process it with conversion tools we provide in this repository. Please refer to [conversion tools](https://github.com/RUCAIBox/RecDatasets/tree/master/conversion_tools).

2. Directly download the processed atomic files. [Baidu Wangpan](https://pan.baidu.com/s/1p51sWMgVFbAaHQmL4aD_-g) (Password: e272), [Google Drive](https://drive.google.com/drive/folders/1so0lckI6N6_niVEYaBu-LIcpOdZf99kj?usp=sharing).


## Datasets link and brief introduction

### Shopping
- [Amazon](http://jmcauley.ucsd.edu/data/amazon/):
  Amazon Review Data includes reviews (ratings, text, helpfulness votes) and product metadata (descriptions, category information, price, brand, and image features), which includes a previous version in 2014 and an updated version in 2018. 
  Our processed datasets are detailed [here](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Amazon).
  - [Amazon 2014](http://jmcauley.ucsd.edu/data/amazon/): This dataset contains product reviews and metadata from Amazon, including 24 categories and 142.8 million reviews spanning May 1996 - July 2014. 
  - [Amazon 2018](https://nijianmo.github.io/amazon/index.html): This Dataset is an updated version of the [Amazon review dataset](http://jmcauley.ucsd.edu/data/amazon/index_2014.html) released in 2014. The total number of reviews is 233.1 million and the number of categories is 29 (142.8 million and 24 in 2014) and current data includes reviews in the range May 1996 - Oct 2018. 
- [Alibaba-iFashion](https://github.com/wenyuer/POG):
  This dataset is a fashion outfit dataset collected from [Alibaba]([https://www.alibaba.com/) online shopping systems in the paper [POG](https://dl.acm.org/doi/10.1145/3292500.3330652). The items from each outfit are viewed as the items being recommended to users, where each item consists of attributes such as category and title.
- [Epinions](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data):
  This dataset was collected from Epinions.com, a popular online consumer review website. It contains trust relationships amongst users and spans more than a decade, from January 2001 to November 2013.
- [Yelp](https://www.yelp.com/dataset):
  This dataset was collected from [Yelp](https://www.yelp.com/). The Yelp dataset is a subset of our businesses, reviews, and user data for use in personal, educational, and academic purposes. 
  Starting from Yelp Challenge 2018 ([the original link](https://www.yelp.com/dataset/challenge) to this competition is not found and there will not be another round of Yelp Dataset Challenge), there are four versions of Yelp datasets in total and Yelp has also posted the dataset on [Kaggle](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset), where you can also download a few earlier versions. 
  Our processed 5 datasets are detailed [here](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Yelp).
  - [Yelp 2018](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/download?datasetVersionNumber=1): It is the first version of Yelp dataset released in Yelp Challenge 2018 including 5,261,669 reviews.
  - [Yelp 2020](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/download?datasetVersionNumber=2): It is the second version of Yelp dataset released in 2020, including 8,021,122 reviews.
  - [Yelp 2021](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/download?datasetVersionNumber=3): It is the first version of Yelp dataset released in 2021, including 8,635,403 reviews.
  - [Yelp 2022](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/download?datasetVersionNumber=4): It is the latest version of Yelp dataset, which contains 908,915 tips by 1,987,897 users over 1.2 million business attributes like hours, parking, availability, and ambience aggregated check-ins over time for each of the 131,930 businesses.
  - Yelp-full: This is a combination dataset including four versions of yelp datasets mentioned above, where the duplicates are dropped and the number of total reviews is 28,908,240.
- [Tmall](https://tianchi.aliyun.com/dataset/dataDetail?dataId=53):
  This dataset is provided by Ant Financial Services, using in the IJCAI16 contest.
- [DIGINETICA](https://competitions.codalab.org/competitions/11161):
  The dataset includes user sessions extracted from an e-commerce search engine logs, with anonymized user ids,
  hashed queries, hashed query terms, hashed product descriptions and meta-data, log-scaled prices, clicks, and purchases.
- [YOOCHOOSE](https://2015.recsyschallenge.com/challenge.html):
  This dataset was constructed by YOOCHOOSE GmbH to support participants in the RecSys Challenge 2015.
- [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset):
  The data has been collected from a real-world ecommerce website. It is raw data, i.e.
  without any content transformations, however, all values are hashed due to confidential issues.
- [Ta Feng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset):
  The dataset contains a Chinese grocery store transaction data from November 2000 to February 2001.

### Advertising
* [Criteo](https://www.kaggle.com/c/criteo-display-ad-challenge/data):
  This dataset was collected from Criteo, which consists of a portion of Criteo's traffic over a period of several days.
  
* [Avazu](https://www.kaggle.com/c/avazu-ctr-prediction/data):
  This dataset is used in Avazu CTR prediction contest.
  
* [iPinYou](http://contest.ipinyou.com): 
  This dataset was provided by iPinYou, which contains all training datasets and leaderboard testing datasets of the three seasons iPinYou Global RTB(Real-Time Bidding) Bidding Algorithm Competition.

* [AliEC](https://tianchi.aliyun.com/dataset/dataDetail?dataId=56#1):
  Ali_Display_Ad_Click is a dataset of click rate prediction about display Ad, which is displayed on the website of Taobao. The dataset is offered by the company of [Alibaba](https://www.alibaba.com/). 

### Check-in
* [Foursquare](https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset):
  This dataset contains check-ins in NYC and Tokyo collected for about 10 month. 
  Each check-in is associated with its time stamp, its GPS coordinates and its semantic meaning.

* [Gowalla](https://snap.stanford.edu/data/loc-gowalla.html):
This dataset is from a location-based social networking website where users share their locations by checking-in, and contains a total of 6,442,890 check-ins of these users over the period of Feb. 2009 - Oct. 2010.

### Movies
- [MovieLens](https://grouplens.org/datasets/movielens/):
GroupLens Research has collected and made available rating datasets from their movie website.
- [Netflix](https://www.kaggle.com/netflix-inc/netflix-prize-data):
This is the official data set used in the Netflix Prize competition.
- [Douban](https://www.kaggle.com/utmhikari/doubanmovieshortcomments):
Douban Movie is a Chinese website that allows Internet users to share their comments and viewpoints about movies.
This dataset contains more than 2 million short comments of 28 movies in Douban Movie website.
- [Twitch](https://cseweb.ucsd.edu/~jmcauley/datasets.html#twitch):
  This is a dataset of users consuming streaming content on [Twitch](https://www.twitch.tv). We retrieved all streamers, and all users connected in their respective chats, every 10 minutes during 43 days.
  - Twitch-100k: Twitch-100k is a subset of 100k users for benchmark purposes. The code is available in this [Github repository](https://www.google.com/url?q=https://github.com/JRappaz/liverec&source=gmail-html&ust=1629428377164000&usg=AFQjCNFEGBZtyMwP3RJu-w8IWbubR8MAjw).
  - Twitch-full: See the [Google Drive folder](https://www.google.com/url?q=https://drive.google.com/drive/folders/1BD8m7a8m7onaifZay05yYjaLxyVV40si?usp%3Dsharing&source=gmail-html&ust=1629428377164000&usg=AFQjCNFXimN1hHftvhgIu5iKUTZiOsep8A) containing all Twitch files. Twitch-full contains the full dataset while Twitch-100k is a subset.

### Music
- [Last.FM](https://grouplens.org/datasets/hetrec-2011/):
This dataset contains social networking, tagging, and music artist listening information from a set of 2K users from Last.fm online music system.
- [LFM-1b](http://www.cp.jku.at/datasets/LFM-1b/):
This dataset contains more than one billion music listening events created by more than 120,000 users of Last.FM.
Each listening event is characterized by artist, album, and track name, and includes a timestamp.
- [Yahoo Music](https://webscope.sandbox.yahoo.com/catalog.php?datatype=r):
This dataset represents a snapshot of the Yahoo! Music community's preferences for various musical artists.
- [KGRec](https://www.upf.edu/web/mtg/kgrec):
  Music and Sound Recommendation with Knowledge Graphs are two different datasets with users, items, implicit feedback interactions between users and items, item tags, and item text descriptions are provided, one for Music Recommendation (KGRec-music), and other for Sound Recommendation (KGRec-sound). 
  - KGRec-music: All the data comes from `songfacts.com` and `last.fm` websites. Items are songs, which are described in terms of textual description extracted from `songfacts.com`, and tags from `last.fm`.
  - KGRec-sound: All the data comes from `Freesound.org`. Items are sounds, which are described in terms of textual description and tags created by the sound creator at uploading time.

### Books
* [Book-Crossing](http://www2.informatik.uni-freiburg.de/~cziegler/BX/):
This dataset was collected by Cai-Nicolas Ziegler in a 4-week crawl (August / September 2004) from the [Book-Crossing](http://www.bookcrossing.com/) community with kind permission from Ron Hornbaker, CTO of [Humankind Systems](http://www.humankindsystems.com/). 
It contains 278,858 users (anonymized but with demographic information) providing 1,149,780 ratings (explicit / implicit) about 271,379 books.

* [GoodReads](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home/):
This dataset contain reviews from the [Goodreads](https://www.goodreads.com) book review website, and a variety of attributes describing the items. Critically, datasets have multiple levels of user interaction, raging from adding to a shelf, rating, and reading.

### Games
* [Steam](https://github.com/kang205/SASRec):
This dataset is reviews and game information from Steam, which contains 7,793,069 reviews, 2,567,538 users, and 32,135 games. 
In addition to the review text, the data also includes the users' play hours in each review.

### Anime
- [Anime](https://www.kaggle.com/CooperUnion/anime-recommendations-database):
This dataset contains information on user preference data from [MyAnimeList.net - Anime and Manga Database and Community](https://myanimelist.net). 
Each user is able to add anime to their completed list and give it a rating and this dataset is a compilation of those ratings.

### Pictures
* [Pinterest](https://github.com/hexiangnan/neural_collaborative_filtering/tree/master/Data):
This dataset is originally constructed by paper Learning image and user features for recommendations in social networks for evaluating content-based image recommendation, and processed by paper Neural Collaborative Filtering.

### Jokes
* [Jester](http://eigentaste.berkeley.edu/dataset/):
This dataset contains anonymous ratings of jokes by users of the Jester Joke Recommender System.

### Exercises
* [KDD2010](https://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp):
This dataset was released in KDD Cup 2010 Educational Data Mining Challenge, which contains the situations of students submitting exercises on the systems.

* [EndoMondo](https://cseweb.ucsd.edu/~jmcauley/datasets.html#endomondo):
This is a collection of workout logs from users of [EndoMondo](https://www.endomondo.com/). 
Data includes multiple sources of sequential sensor data such as heart rate logs, speed, GPS, as well as sport type, gender and weather conditions.

### Websites
* [Phishing Websites](http://archive.ics.uci.edu/ml/datasets/Phishing+Websites):
This dataset contains 30 kinds of features of 11,055 websites and labels of whether they are phishing websites or not.
The websites' features includes 12 address-bar based features, 6 abnormal based features, 5 HTML-and-JavaScript based features and 7 domain based features.

* [Behance](https://cseweb.ucsd.edu/~jmcauley/datasets.html#behance):
This is a small, anonymized, version of a larger proprietary dataset about likes and image data from the community art website [Behance](https://www.behance.net).

### Adult
* [Adult](http://archive.ics.uci.edu/ml/datasets/Adult):
This dataset is extracted by Barry Becker from the 1994 Census database, which consists of a list of
people's attributes and whether they make over 50k a year.

### News
* [MIND](https://msnews.github.io/):
This dataset is a large-scale dataset for news recommendation research. It was collected from anonymized behavior logs of [Microsoft News website](https://news.microsoft.com). 
MIND contains about 160k English news articles and more than 15 million impression logs generated by 1 million users.

### Food
* [DianPing](http://yongfeng.me/dataset/):
This dataset contains the user reviews as well as the detailed business meta data information crawled from a famous Chinese online review webset [DianPing.com](http://www.dianping.com/), including the 3,605,300 reviews of 510,071 users towards 209,132 businesses.

* [Food](https://cseweb.ucsd.edu/~jmcauley/datasets.html#foodcom):
These datasets contain recipe details and reviews from [Food.com](https://cseweb.ucsd.edu/~jmcauley/www.food.com) (formerly GeniusKitchen). Data includes cooking recipes and review texts.

### Beverages
* [BeerAdvocate](https://cseweb.ucsd.edu/~jmcauley/datasets.html#multi_aspect):
This dataset includes beer reviews with multiple rated dimensions, covering sensory aspects such as taste, look, feel, and smell.
* [RateBeer](https://cseweb.ucsd.edu/~jmcauley/datasets.html#multi_aspect):
This dataset contains beer reviews with multiple rated dimensions, including item attributes with sensory aspects such as taste, look, feel, and smell.

### Clothes
* [ModCloth](https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit):
These datasets contain measurements of clothing fit from ModCloth.
* [RentTheRunway](https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit):
These datasets contain measurements of clothing fit from [RentTheRunway](https://www.renttherunway.com).


## Datasets information statistics

### General Datasets

| SN | Dataset           | \#User    | \#Item    | \#Inteaction | Sparsity | Interaction Type           | TimeStamp | User Context | Item Context | Interaction Context |
|----|-------------------|-----------|-----------|--------------|----------|----------------------------|-----------|--------------|--------------|---------------------|
| 1  | [MovieLens](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/MovieLens)         | \-        | \-        | \-           | \-       | Rating                     | √         | √            | √            |                     |
| 2  | Anime             | 73,515    | 11,200    | 7,813,737    | 99\.05%  | Rating <br> \[\-1, 1\-10\] |           |              | √            |                     |
| 3  | Epinions          | 116,260   | 41,269    | 188,478      | 99\.99%  | Rating <br> \[1\-5\]       | √         |              |              | √                   |
| 4  | [Yelp](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Yelp)<br>(5 versions) | \-        | \-        | \-            | \-       | Rating <br> \[1\-5\]       | √         | √            | √            | √                   |
| 5  | Netflix           | 480,189   | 17,770    | 100,480,507  | 98\.82%  | Rating <br> \[1\-5\]       | √         |              |              |                     |
| 6  | Book\-Crossing   | 105,284   | 340,557   | 1,149,780    | 99\.99%  | Rating <br> \[0\-10\]      |           | √            | √            |                     |
| 7  | Jester            | 73,421    | 101       | 4,136,360    | 44\.22%  | Rating <br> \[\-10, 10\]   |           |              |              |                     |
| 8  | Douban            | 738,701   | 28        | 2,125,056    | 89\.73%  | Rating <br> \[0,5\]        | √         |              |              | √                   |
| 9  | Yahoo Music       | 1,948,882 | 98,211    | 11,557,943   | 99\.99%  | Rating <br> \[0, 100\]     |           |              | √            |                     |
| 10 | [KDD2010](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/KDD2010)           | \-        | \-        | \-           | \-       | Rating                     |           |              |              | √                   |
| 11 | [Amazon](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Amazon)<br>(2014 & 2018) | \-        | \-        | \-           | \-       | Rating<br/> \[0,5\]        | √         |              | √            |                     |
| 12 | Pinterest         | 55,187    | 9,911     | 1,445,622    | 99\.74%  | \-                         |           |              |              |                     |
| 13 | [Gowalla](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Gowalla)           | 107,092   | 1,280,969 | 6,442,892   | 99\.99%  | Check-in                   | √         |              |              | √                   |
| 14 | Last.FM           | 1,892     | 17,632    | 92,834       | 99\.72%  | Click                      |           |              |              | √                   |
| 15 | [DIGINETICA](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/DIGINETICA)        | 204,789 | 184,047   | 993,483      | 99\.99%  | Click                      | √         |              | √            |                     |
| 16 | [Steam](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Steam)             | 2,567,538 | 32,135    | 7,793,069    | 99\.99%  | Buy                        | √         |              | √            | √                   |
| 17 | [Ta Feng](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/TaFeng)           | 32,266    | 23,812    | 817,741      | 99\.89%  | Click                      | √         | √            | √            | √                   |
| 18 | [Foursquare](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Foursquare)      | \-        | \-        | \-           | \-       | Check-in                   | √         |              | √            |                     |
| 19 | [Tmall](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Tmall)             | 963,923 | 2,353,207 | 44,528,127 | 99.99% | Click/Buy                  | √         |              |              | √                   |
| 20 | [YOOCHOOSE](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/YOOCHOOSE)         | 9,249,729  | 52,739    | 34,154,697    | 99.99%   | Click/Buy                  | √         |              |              | √                   |
| 21 | [Retailrocket](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Retailrocket)      | 1,407,580  | 247,085   | 2,756,101     | 99.99%   | View/Addtocart/Transaction | √         |              |              |                     |
| 22 | [LFM-1b](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/LFM-1b)            | 120,322   | 3,123,496 | 1,088,161,692   | 99\.71%  | Click                      | √         | √            | √            | √                   |
| 23 | [MIND](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/MIND) | - | - | - | - | Click | √ | |  |  |
| 24 | BeerAdvocate      | 33,388     | 66,055 | 1,586,614    | 99\.9281% | Rating<br/> \[0,5\] | √ | | √ |  |
| 25 | Behance                                      | 63,497     | 178,788 | 1,000,000   | 99\.9912% | Likes | √ | | √ |  |
| 26 | DianPing                                     | 542,706    | 243,247 | 4,422,473   | 99\.9967% | Rating<br/> \[0,5\] | √ | | √ | √ |
| 27 | EndoMondo                                     | 1,104      | 253,020  | 253,020  | 99\.9094% | Workout Logs | √ | √ |  | √ |
| 28 | Food                                        | 226,570    | 231,637   | 1,132,367 | 99\.9978% | Rating<br/> \[0,5\] | √ |  | √ |  |
| 29 | GoodReads                               | 876,145    | 2,360,650    | 228,648,342 | 99\.9889% | Rating<br/> \[0,5\] | √ |  | √ |  |
| 30 | [KGRec](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/KGRec) | - | - | - | - | Click | | | √ |  |
| 31 | ModCloth                                      | 47,958     | 1,378      | 82,790 | 99\.8747% | Rating<br/> \[0,5\] | | √ | √ | √ |
| 32 | RateBeer                                  | 29,265     | 110,369    | 2,924,163  | 99\.9095% | Overall Rating<br/> \[0,20\] | √ | | √ | √ |
| 33 | RentTheRunway                              | 105,571    | 5,850      | 192,544   | 99\.9688% | Rating<br/> \[0,10\] | √ | √ | √ | √ |
| 34 | [Twitch](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/Twitch)  | 15,524,309 | 6,161,666 | 474,676,929  | 99\.9995% | Click | | |  | √ |


### CTR Datasets

| SN | Dataset           | \#User    | \#Item    | \#Inteaction | Sparsity | Interaction Type           | TimeStamp | User Context | Item Context | Interaction Context |
|----|:------------------|-----------|-----------|--------------|----------|----------------------------|-----------|--------------|--------------|---------------------|
| 1  | Criteo            | \-        | \-        | 45,850,617   | \-       | Click                      |           |              |              | √                   |
| 2  | Avazu             | \-        | \-        | 40,428,967   | \-       | Click <br> \[0, 1\]        | √         |              |              | √                   |
| 3  | [iPinYou](https://github.com/RUCAIBox/RecommenderSystems-Datasets/tree/master/dataset_info/iPinYou)   | 19,731,660 | 163 | 24,637,657 | 99.23% | View/Click                 |           | √            | √            | √                   |
| 4  | Phishing websites | -        | \-        | 11,055       | \-       |                            |           |              |              | √                   |
| 5  | Adult             | \-        | \-        | 32,561       | \-       | income>=50k <br> \[0, 1\]  |           |              |              | √                   |
| 6  | Alibaba-iFashion  | 3,569,112  | 4,463,302  | 191,394,393 | 99\.9988% | Click |  | | √ |  |
| 7  | AliEC             | 491,647    | 240,130    | 1,366,056   | 99\.9988% | Click | √ | √ | √ |  |


### Knowledge-aware Datasets
These knowledge-aware recommender datasets are based on [KB4Rec](https://github.com/RUCDM/KB4Rec),
which associate items from recommender systems with entities from Freebase.

Raw datasets information

| SN | Dataset            | \#Items    | \#Linked\-Items | \#Users   | \#Interactions |
|----|--------------------|------------|-----------------|-----------|----------------|
| 1  | MovieLens          | 27,278     | 25,503          | 138,493   | 20,000,263     |
| 2  | Amazon\-book       | 2,370,605  | 108,515         | 8,026,324 | 22,507,155     |
| 3  | LFM\-1b \(tracks\) | 31,634,450 | 1,254,923       | 120,322   | 319,951,294    |

After filtering by 5-core (And filter out the tracks that are listened to less than 10 times in LFM-1b)

| SN | Dataset            | \#Items | \#Linked\-Items | \#Users | \#Interactions |
|----|--------------------|---------|-----------------|---------|----------------|
| 1  | MovieLens          | 18,345  | 18,057          | 138,493 | 19,984,024     |
| 2  | Amazon\-book       | 367,982 | 34,476          | 603,668 | 8,898,041      |
| 3  | LFM\-1b \(tracks\) | 615,823 | 337,349         | 79,133  | 15,765,756     |

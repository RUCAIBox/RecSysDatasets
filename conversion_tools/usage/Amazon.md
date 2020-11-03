# Amazon

**It should be noted that this series of datsets is divided into many sub-datasets according to the categories of Amazon products. You can download the corresponding data set files according to your needs. We will demonstrate the operation steps of 'Amazon_Video_Games' dataset below, and you can process sub-datasets of other categories according to the demonstration.**

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Amazon dataset and extract the dataset file.**

(If you have already done this, please move to the step 3.)

You can download ratings only data and metadata from http://jmcauley.ucsd.edu/data/amazon/.

However, we're sorry for the metadata before 2014 we used can't be downloaded from the website now. We will continue with the assumption that the operator already has the original metadata. If you don't have the original metadata, you can download processed data from  [Baidu Yun](https://pan.baidu.com/s/1p51sWMgVFbAaHQmL4aD_-g) or [Google Drive](https://drive.google.com/drive/folders/1so0lckI6N6_niVEYaBu-LIcpOdZf99kj?usp=sharing).

Here we download ratings_Video_Games.csv and meta_Video_Games.json.gz,

save them in current folder(Amazon_Video_Games/), and do:

```
gunzip meta_Video_Games.json.gz
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Amazon_Video_Games dataset.**

```
python run.py --dataset amazon_video_games \
--input_path Amazon_Video_Games --output_path output_data/Amazon_Video_Games \
--convert_inter --convert_item
```

`input_path` is the path of the input decompressed Amazon_Video_Games file

`output_path` is the path to store converted atomic files

 `convert_inter` Amazon_Video_Games can be converted to '*.inter' atomic file

 `convert_item` Amazon_Video_Games can be converted to '*.inter' atomic file


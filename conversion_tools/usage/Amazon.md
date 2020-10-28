# Amazon

**It should be noted that this series of data sets is divided into many sub-data sets according to the categories of Amazon products. You can download the corresponding data set files according to your needs. We will demonstrate the operation mode of 'Amazon_Video_Games' dataset below, and you can process the sub-data sets of other categories in this series according to the demonstration.**

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

Here we download ratings_Video_Games.csv and meta_Video_Games.json.gz

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


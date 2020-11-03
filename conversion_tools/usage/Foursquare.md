# Foursquare

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Foursquare Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

In this step, you need to log in to kaggle and download data from https://www.kaggle.com/chetanism/foursquare-nyc-and-tokyo-checkin-dataset.

The download is a compressed file which named 'archive.zip', and in this file there are two files named 'dataset_TSMC2014_NYC.csv' and 'dataset_TSMC2014_TKY.csv'.

```
unzip archive.zip -d ./foursquare-data
rm archive.zip
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Foursquare  dataset.**

```
# if duplicate_removal
python run.py --dataset foursquare --input_path foursquare-data --output_path output_data/foursquare --duplicate_removal --convert_inter

# if not duplicate_removal
python run.py --dataset foursquare --input_path foursquare-data --output_path output_data/foursquare --convert_inter

python run.py --dataset foursquare --input_path foursquare-data --output_path output_data/foursquare --convert_item
```

`input_path` is the path of the input decompressed Foursquare file

`output_path` is the path to store converted atomic files

`dupliacte_removal` The interaction type in Foursquare data is check-in, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.

`convert_inter` Foursquare can be converted to '*.inter' atomic file

`convert_item` Foursquare can be converted to '*.item' atomic file

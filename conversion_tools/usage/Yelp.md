# Yelp

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the [Yelp](https://www.yelp.com/dataset) Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
# Download the Yelp Dataset into the 'conversion_tools/' directory.

mkdir yelp_dataset

tar -zxvf yelp_dataset.tar -C ./yelp_dataset
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Yelp dataset.**

```
python run.py --dataset yelp \
--input_path yelp_dataset --output_path output_data/yelp \
--convert_inter --convert_item --convert_user
```

`input_path` is the path of the input decompressed Yelp file

`output_path` is the path to store converted atomic files

 `convert_inter` Yelp can be converted to '*.inter' atomic file

`convert_item` Yelp can be converted to '*.item' atomic file

`convert_user` Yelp can be converted to '*.user' atomic file
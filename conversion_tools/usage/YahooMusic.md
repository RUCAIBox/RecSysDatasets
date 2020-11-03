# Yahoo Music

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the [Yahoo Music](https://webscope.sandbox.yahoo.com/catalog.php?datatype=r) Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
# Download the Yahoo Music Dataset into the 'conversion_tools/' directory.
# Dataset Name: R1 - Yahoo! Music User Ratings of Musical Artists, version 1.0 (423 MB)

mkdir yahoo-music

tar -zxvf dataset.tgz -C ./yahoo-music
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Yahoo Music dataset.**

```
python run.py --dataset yahoo-music \
--input_path yahoo-music --output_path output_data/yahoo-music \
--convert_inter --convert_item
```

`input_path` is the path of the input decompressed Yahoo Music file

`output_path` is the path to store converted atomic files

 `convert_inter` Yahoo Music can be converted to '*.inter' atomic file

`convert_item` Yahoo Music can be converted to '*.item' atomic file
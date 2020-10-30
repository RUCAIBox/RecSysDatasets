# Douban

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Douban Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

In this step, you need to log in to kaggle and download data from https://www.kaggle.com/utmhikari/doubanmovieshortcomments.

The download is a compressed file which named 'archive.zip', and in this file there are one file named 'DMSC.csv' and its size is about 405MB.

```
unzip archive.zip -d ./douban-data
rm -rvf archive.zip
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Douban dataset.**

```
python run.py --dataset douban --input_path douban-data --output_path output_data/douban --convert_inter
```

`input_path` is the path of the input decompressed Douban file.

`output_path` is the path to store converted atomic files.

`convert_inter` Douban only can be converted to '*.inter' atomic file.


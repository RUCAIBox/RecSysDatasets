# Anime

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Anime Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

You can download dataset(archive.zip) from https://www.kaggle.com/CooperUnion/anime-recommendations-database, 
save it in current folder, and do:

```
unzip archive.zip -d anime-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Anime dataset.**

```
python run.py --dataset anime \ 
--input_path anime-data --output_path output_data/anime \
--convert_inter --convert_item
```

`input_path` is the path of the input decompressed Anime file

`output_path` is the path to store converted atomic files
 
 `convert_inter` Anime can be converted to '*.inter' atomic file

 `convert_item` Anime can be converted to '*.item' atomic file

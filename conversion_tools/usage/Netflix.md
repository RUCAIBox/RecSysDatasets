# Netflix

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Netflix Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
please go to https://www.kaggle.com/netflix-inc/netflix-prize-data, and
click 'Download' to get archive.zip. Then place archive.zip in directory
'conversion_tools/'.

unzip -o -d ./netflix-data archive.zip
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Netflix dataset.**

```
python run.py --dataset netflix \
--input_path netflix-data --output_path output_data/netflix \
--convert_inter
```

`input_path` is the path of the input decompressed Netflix file

`output_path` is the path to store converted atomic files

`convert_inter` Netflix only can be converted to '*.inter' atomic file

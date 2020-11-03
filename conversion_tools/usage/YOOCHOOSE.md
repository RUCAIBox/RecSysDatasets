# YOOCHOOSE

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the YOOCHOOSE Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
wget https://s3-eu-west-1.amazonaws.com/yc-rdata/yoochoose-data.7z

7z x yoochoose-data.7z -o./yoochoose-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of YOOCHOOSE dataset.**

```
python run.py --dataset yoochoose \
--input_path yoochoose-data --output_path output_data/yoochoose \
--interaction_type buy --duplicate_removal \
--convert_inter
```

`input_path` is the path of the input decompressed YOOCHOOSE file

`output_path` is the path to store converted atomic files

`interaction_type` YOOCHOOSE data contains two types of interaction: click and buy.
You can choose one of them to generate the corresponding atomic file. Range in [click, buy]

 `dupliacte_removal` The interaction type in YOOCHOOSE data is click/buy, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.

 `convert_inter` YOOCHOOSE only can be converted to '*.inter' atomic file

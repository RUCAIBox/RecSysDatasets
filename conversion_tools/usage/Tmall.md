# Tmall

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Tmall Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
please go to https://tianchi.aliyun.com/dataset/dataDetail?dataId=53 to
download 'IJCAI16_data.zip' and place it in directory 'conversion_tools/'

unzip -d IJCAI16_data.zip

mv IJCAI16_data tmall-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Tmall dataset.**

```
python run.py --dataset tmall \
--input_path tmall-data --output_path output_data/tmall \
--interaction_type buy --duplicate_removal \
--convert_inter
```

`input_path` is the path of the input decompressed Tmall file

`output_path` is the path to store converted atomic files

`interaction_type` Tmall data contains two type interactions: click and buy.
You can choose one of them to generate the corresponding atomic file. Range in [click, buy]
 
 `dupliacte_removal` The interaction type in Tmall data is click/buy, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.
 
 `convert_inter` Tmall only can be converted to '*.inter' atomic file

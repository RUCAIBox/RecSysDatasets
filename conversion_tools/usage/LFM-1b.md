# LFM-1b

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the LFM-1b Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

You can download dataset(LFM-1b.zip) from http://www.cp.jku.at/datasets/LFM-1b, 
save it in current folder, and do:

```
unzip LFM-1b.zip -d lfm1b-data/
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of LFM-1b dataset.**

```
python run.py --dataset lfm1b \ 
--input_path lfm1b-data --output_path output_data/lfm1b \
--interaction_type artists --duplicate_removal \ 
--convert_inter --convert_item --convert_user
```

`input_path` is the path of the input decompressed LFM-1b file

`output_path` is the path to store converted atomic files

`interaction_type` LFM-1b data contains three type interactions: users listen to artists, 
users listen to albums, users listen to tracks. You can choose one of them to generate 
the corresponding atomic file. Range in [artists, albums, tracks]
 
 `dupliacte_removal` The interaction type in LFM-1b data is click, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.
 
 `convert_inter` LFM-1b can be converted to '*.inter' atomic file

 `convert_item` LFM-1b can be converted to '*.item' atomic file

 `convert_user` LFM-1b can be converted to '*.user' atomic file

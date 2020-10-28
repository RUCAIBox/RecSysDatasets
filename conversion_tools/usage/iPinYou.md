# iPinYou

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the iPinYou Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

please go to https://pan.baidu.com/s/1kTwX2mF#list/path=%2F to download
'ipinyou.contest.dataset' and place it in directory 'conversion_tools/'

```
mkdir ipinyou-data

mv ipinyou.contest.dataset/training* ipinyou-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of iPinYou dataset.**

```
python run.py --dataset ipinyou \
--input_path ipinyou-data --output_path output_data/ipinyou \
--interaction_type view --duplicate_removal \
--convert_inter
```

`input_path` is the path of the input decompressed iPinYou file

`output_path` is the path to store converted atomic files

`interaction_type` iPinYou data contains two type interactions: click and view.
You can choose one of them to generate the corresponding atomic file. Range in [click, view]
 
 `dupliacte_removal` The interaction type in iPinYou data is click/view, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.
 
`convert_inter` iPinYou can be converted to '*.inter' atomic file
 
`convert_item` iPinYou can be converted to '*.item' atomic file
  
`convert_user` iPinYou can be converted to '*.user' atomic file

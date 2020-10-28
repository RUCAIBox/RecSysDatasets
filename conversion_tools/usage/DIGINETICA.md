# DIGINETICA

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the DIGINETICA Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

Download from https://drive.google.com/open?id=0B7XZSACQf0KdXzZFS21DblRxQ3c and we only use the following files:

'products.csv', 'product-categories.csv', 'train-item-views.csv'

Create a folder 'diginetica-data' and put them in it.

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of DIGINETICA dataset.**

```
# if duplicate_removal
python run.py --dataset diginetica --input_path diginetica-data --output_path output_data/diginetica --duplicate_removal --convert_inter

# if not duplicate_removal
python run.py --dataset diginetica --input_path diginetica-data --output_path output_data/diginetica --convert_inter

python run.py --dataset diginetica --input_path diginetica-data --output_path output_data/diginetica --convert_item
```

`input_path` is the path of the input decompressed DIGINETICA file

`output_path` is the path to store converted atomic files

`dupliacte_removal` There may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.

`convert_inter` DIGINETICA can be converted to '*.inter' atomic file

`convert_item` DIGINETICA can be converted to '*.item' atomic file
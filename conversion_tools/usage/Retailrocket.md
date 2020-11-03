# Retailrocket

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the [Retailrocket](https://www.kaggle.com/retailrocket/ecommerce-dataset) Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
# Download the Retailrocket Dataset into the 'conversion_tools/' directory.

unzip archive.zip -d ./retailrocket
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Retailrocket dataset.**

```
python run.py --dataset retailrocket \
--input_path retailrocket --output_path output_data/retailrocket \
--interaction_type view --duplicate_removal \
--convert_inter --convert_item
```

`input_path` is the path of the input decompressed Retailrocket file

`output_path` is the path to store converted atomic files

`interaction_type` Retailrocket data contains three types of interaction: view, addtocart and transaction.
You can choose one of them to generate the corresponding atomic file. Range in [view, addtocart, transaction]

 `dupliacte_removal` The interaction type in Retailrocket data is view/addtocart/transaction, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.

 `convert_inter` Retailrocket can be converted to '*.inter' atomic file

`convert_item` Retailrocket can be converted to '*.item' atomic file
# Steam

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Steam Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
wget http://cseweb.ucsd.edu/~wckang/steam_reviews.json.gz
wget http://cseweb.ucsd.edu/~wckang/steam_games.json.gz

mkdir steam-data
gunzip -c steam_reviews.json.gz > steam-data/steam_reviews.json
gunzip -c steam_games.json.gz > steam-data/steam_games.json

rm -rvf steam_reviews.json.gz
rm -rvf steam_games.json.gz
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Steam dataset.**

```
# if duplicate_removal
python run.py --dataset steam --input_path steam-data --output_path output_data/steam --duplicate_removal --convert_inter

# if not duplicate_removal
python run.py --dataset steam --input_path steam-data --output_path output_data/steam --convert_inter

python run.py --dataset steam --input_path steam-data --output_path output_data/steam --convert_item
```

`input_path` is the path of the input decompressed Steam file.

`output_path` is the path to store converted atomic files.

`dupliacte_removal` There may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.

`convert_inter` Steam can be converted to '*.inter' atomic file.

`convert_inter` Steam can be converted to '*.item' atomic file.
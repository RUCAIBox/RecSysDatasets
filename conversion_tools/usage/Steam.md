# Steam

1.Clone the repository and install requirements. 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.Download the Steam Dataset and extract the dataset file.
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

3.Go the ``conversion_tools/`` directory 
and run the following command to get the Atomic files of Steam dataset.

```
python run.py --dataset steam --input_path steam-data --output_path output_data/steam-data --convert_inter

python run.py --dataset steam --input_path steam-data --output_path output_data/steam-data --convert_item
```

`input_path` is the path of the input decompressed Steam file.

`output_path` is the path to store converted atomic files.

 `convert_inter` Steam can be converted to '*.inter' atomic file.

`convert_inter` Steam can be converted to '*.item' atomic file.

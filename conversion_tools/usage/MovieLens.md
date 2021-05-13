# MovieLens

This dataset has several sub-datasets of different sizes, 
respectively 'ml-100k',  'ml-1m', 'ml-10m' and 'ml-20m'. 
You can download the corresponding dataset files according 
to your needs.


1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the MovieLens dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

Here we process all of 4 datasets, and you can download corresponding dataset according to your neads.

```
wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
unzip ml-100k -d ml-100k

wget http://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip -d ml-1m

wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
unzip ml-10m.zip -d ml-10m

wget http://files.grouplens.org/datasets/movielens/ml-20m.zip
unzip ml-20m.zip -d ml-20m
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of  MovieLens dataset.**

```
python run.py --dataset ml-100k \ 
--input_path ml-100k --output_path output_data/ml-100k \
--convert_inter --convert_item --convert_user

python run.py --dataset ml-1m \ 
--input_path ml-1m --output_path output_data/ml-1m \
--convert_inter --convert_item --convert_user

python run.py --dataset ml-10m \ 
--input_path ml-10m --output_path output_data/ml-10m \
--convert_inter --convert_item 

python run.py --dataset ml-20m \ 
--input_path ml-20m --output_path output_data/ml-20m \
--convert_inter --convert_item 
```

`input_path` is the path of the input decompressed MovieLen file

`output_path` is the path to store converted atomic files

`convert_inter` ml-100k, ml-1m, ml-10m and ml-10m all can be converted to '*.inter' atomic file

`convert_item` ml-100k, ml-1m, ml-10m and ml-10m can be converted to '*.item' atomic file

`convert_user` ml-100k, ml-1m can be converted to '*.user' atomic file


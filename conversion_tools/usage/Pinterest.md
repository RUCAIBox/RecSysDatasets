# Pinterest

1.Clone the repository and install requirements. 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.Download the Pinterest Dataset and extract the dataset file.
(If you have already done this, please move to the step 3.)

```
wget https://raw.githubusercontent.com/hexiangnan/neural_collaborative_filtering/master/Data/pinterest-20.train.rating

mkdir pinterest-data

mv pinterest-20.train.rating ./pinterest-data/

(Note that if you have connection error while excuting wget command, please
go straight to https://github.com/hexiangnan/neural_collaborative_filtering
to download the whole project, and then place /Data/pinterest-20.train.rating
in convertion_tools/pinterest-data/)
```

3.Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Pinterest dataset.

```
python run.py --dataset pinterest \
--input_path pinterest-data --output_path output_data/pinterest-data \
--convert_inter
```

`input_path` is the path of the input decompressed pinterest file

`output_path` is the path to store converted atomic files
 
 `convert_inter` Pinterest only can be converted to '*.inter' atomic file

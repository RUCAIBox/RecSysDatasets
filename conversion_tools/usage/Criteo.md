# Criteo

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Criteo Dataset and extract the dataset file.**

(If you have already done this, please move to the step 3.)

```
wget https://s3-eu-west-1.amazonaws.com/kaggle-display-advertising-challenge-dataset/dac.tar.gz

mkdir criteo-data
tar -zxvf dac.tar.gz -C criteo-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Criteo dataset.**

```
python run.py --dataset criteo --input_path criteo-data --output_path output_data/criteo-data --convert_inter
```

`input_path` is the path of the input decompressed Criteo file

`output_path` is the path to store converted atomic files

`convert_inter` Criteo only can be converted to '*.inter' atomic file

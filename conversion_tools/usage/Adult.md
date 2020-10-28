# Adult

1.**Clone the repository and install requirements.**
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Adult Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
wget http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data

mkdir adult-data & mv adult.data ./adult-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Adult dataset.**

```
python run.py --dataset adult \
--input_path adult-data --output_path output_data/adult \
--convert_inter
```

`input_path` is the path of the input decompressed Adult file

`output_path` is the path to store converted atomic files
 
 `convert_inter` Adult only can be converted to '*.inter' atomic file

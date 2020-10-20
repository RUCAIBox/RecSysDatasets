# jester

1.Clone the repository and install requirements. 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.Download the jester Dataset and extract the dataset file.
(If you have already done this, please move to the step 3.)

```
wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_1.zip
wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_2.zip
wget http://eigentaste.berkeley.edu/dataset/jester_dataset_1_3.zip

unzip jester_dataset_1_1.zip -d ./jester-data
unzip jester_dataset_1_2.zip -d ./jester-data
unzip jester_dataset_1_3.zip -d ./jester-data

rm -rvf jester_dataset_1_1.zip
rm -rvf jester_dataset_1_2.zip
rm -rvf jester_dataset_1_3.zip
```

3.Go the ``conversion_tools/`` directory 
and run the following command to get the Atomic files of jester dataset.

```
python run.py --dataset jester --input_path jester-data --output_path output_data/jester-data --convert_inter
```

`input_path` is the path of the input decompressed jester file.

`output_path` is the path to store converted atomic files.

`convert_inter` jester only can be converted to '*.inter' atomic file.
# Epinions

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Epinions Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
wget http://deepyeti.ucsd.edu/jmcauley/datasets/epinions/epinions_data.tar.gz

tar -zxvf epinions_data.tar.gz
mv epinions_data epinions-data
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Epinions dataset.**

```
python run.py --dataset epinions \ 
--input_path epinions-data --output_path output_data/epinions \
--convert_inter
```

`input_path` is the path of the input decompressed Epinions file

`output_path` is the path to store converted atomic files
 
`convert_inter` Epinions only can be converted to '*.inter' atomic file

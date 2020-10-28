# Avazu

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Avazu Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
kaggle competitions download -c avazu-ctr-prediction
(or if you don't have kaggle API, you can go to
https://www.kaggle.com/c/avazu-ctr-prediction/data,
and click 'Download All' to download avazu-ctr-prediction.zip)

unzip -o -d ./avazu-data avazu-ctr-prediction.zip

gzip -d avazu-data/tain.gz
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Avazu dataset.**

```
python run.py --dataset avazu \
--input_path avazu-data --output_path output_data/avazu \
--convert_inter
```

`input_path` is the path of the input decompressed Avazu file

`output_path` is the path to store converted atomic files

`convert_inter` Avazu only can be converted to '*.inter' atomic file

# Myket

1.Clone the repository and install requirements.
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.Download the Myket Dataset and move the dataset files.
(If you have already done this, please move to the step 3.)

```
wget https://raw.githubusercontent.com/erfanloghmani/myket-android-application-market-dataset/main/myket.csv
wget https://raw.githubusercontent.com/erfanloghmani/myket-android-application-market-dataset/main/app_info_sample.csv

mkdir myket-data

mv myket.csv ./myket-data/
mv app_info_sample.csv ./myket-data/
```

3.Go the ``conversion_tools/`` directory
and run the following command to get the atomic files of Myket dataset.

```
python run.py --dataset myket \
--input_path myket-data --output_path output_data/myket-data \
--convert_inter --convert_item
```

`input_path` is the path of the input decompressed Myket file

`output_path` is the path to store converted atomic files

 `convert_inter`, `convert_item` Myket can be converted to 'myket.inter' and 'myket.item' atomic files

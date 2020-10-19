# PHISHING-WEBSITE

1.Clone the repository and install requirements. 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.Download the PHISHING-WEBSITE Dataset and extract the dataset file.
(If you have already done this, please move to the step 3.)

```
wget http://archive.ics.uci.edu/ml/machine-learning-databases/00327/Training%20Dataset.arff

mkdir phishing-website-data 
mv 'Training Dataset.arff' phishing-website-data/
```

3.Go the ``conversion_tools/`` directory 
and run the following command to get the Atomic files of PHISHING-WEBSITE dataset.

```
python run.py --dataset phishing-website \ 
--input_path phishing-website-data --output_path output_data/phishing-website-data \
--convert_inter
```

`input_path` is the path of the input decompressed phishing-website file

`output_path` is the path to store converted atomic files
 
 `convert_inter` PHISHING-WEBSITE only can be converted to '*.inter' atomic file

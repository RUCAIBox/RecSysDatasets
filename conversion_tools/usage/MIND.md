# MIND

This dataset has several sub-datasets of different sizes, 
respectively 'MIND-large',  'MIND-small'. 
You can download the corresponding dataset files according 
to your needs.


1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the MIND dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

Here we process all of five datasets, and you can download corresponding dataset according to your needs. 

Note: In test set, there is no label. So it is not suggested to use here, unless you want to submit it on [MIND](https://msnews.github.io/)
for evaluation. 

```
wget https://mind201910small.blob.core.windows.net/release/MINDlarge_train.zip
unzip MINDlarge_train.zip -d MINDlarge_train

wget https://mind201910small.blob.core.windows.net/release/MINDlarge_dev.zip
unzip MINDlarge_dev.zip -d MINDlarge_dev

wget https://mind201910small.blob.core.windows.net/release/MINDlarge_test.zip
unzip MINDlarge_test.zip -d MINDlarge_test

wget https://mind201910small.blob.core.windows.net/release/MINDsmall_train.zip
unzip MINDsmall_train.zip -d MINDsmall_train

wget https://mind201910small.blob.core.windows.net/release/MINDsmall_dev.zip
unzip MINDsmall_dev.zip -d MINDsmall_dev
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of MIND dataset.**

```
python run.py --dataset mind_large_train \
--input_path MINDlarge_train --output_path output_data/mind_large_train \
--convert_inter 

python run.py --dataset mind_large_dev \
--input_path MINDlarge_dev --output_path output_data/mind_large_dev \
--convert_inter 

python run.py --dataset mind_small_train \
--input_path MINDsmall_train --output_path output_data/mind_small_train \
--convert_inter  

python run.py --dataset mind_small_dev \
--input_path MINDsmall_dev --output_path output_data/mind_small_dev \
--convert_inter 
```

`input_path` is the path of the input decompressed MIND file

`output_path` is the path to store converted atomic files

`convert_inter` MINDlarge_train, MINDlarge_dev, MINDsmall_train and MINDsmall_dev can be converted to '*.inter' atomic file.




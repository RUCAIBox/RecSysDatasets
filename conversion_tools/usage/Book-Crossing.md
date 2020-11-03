# Book-Crossing

1.**Clone the repository and install requirements.**
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Book-Crossing Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
wget http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip

unzip BX-CSV-Dump.zip -d Book-Crossing
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Book-Crossing dataset.**

```
python run.py --dataset book-crossing \
--input_path Book-Crossing --output_path output_data/book-crossing \
--convert_inter --convert_user --convert_item
```

`input_path` is the path of the input decompressed Book-Crossing file

`output_path` is the path to store converted atomic files

 `convert_inter` Book-Crossing can be converted to '*.inter' atomic file

`convert_item` Book-Crossing can be converted to '*.item' atomic file

`convert_user` Book-Crossing can be converted to '*.user' atomic file


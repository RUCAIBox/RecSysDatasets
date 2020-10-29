# Ta Feng

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the [Ta Feng](https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset) Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
# Download the Ta Feng Dataset into the 'conversion_tools/' directory.

unzip archive.zip -d ./ta-feng
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Ta Feng dataset.**

```
python run.py --dataset ta-feng \
--input_path ta-feng --output_path output_data/ta-feng \
--duplicate_removal \
--convert_inter
```

`input_path` is the path of the input decompressed ta-feng file

`output_path` is the path to store converted atomic files

 `dupliacte_removal` There may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.

 `convert_inter` Ta Feng only can be converted to '*.inter' atomic file

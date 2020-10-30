# Gowalla

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the Gowalla Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

```
wget https://snap.stanford.edu/data/loc-gowalla_totalCheckins.txt.gz

mkdir gowalla-data
gzip -d loc-gowalla_totalCheckins.txt.gz
mv loc-gowalla_totalCheckins.txt gowalla-data/
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Gowalla dataset.**

```
python run.py --dataset gowalla \ 
--input_path gowalla-data --output_path output_data/gowalla \
--duplicate_removal \ 
--convert_inter
```

`input_path` is the path of the input decompressed Gowalla file

`output_path` is the path to store converted atomic files
 
 `dupliacte_removal` The interaction type in Gowalla data is check-in, 
 there may be multiple interaction records for the same user-item pair. Add `--dupliacte_removal` can 
 keep only the most recent interaction between user and item and 
 record the number of interactions between the user and the item. 
 If you do not want to do this, please ignore this parameter.
 
 `convert_inter` Gowalla only can be converted to '*.inter' atomic file

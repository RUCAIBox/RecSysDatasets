# Music4All-Onion

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download and extract the Music4All-Onion Dataset files you want to convert.**
(If you have already done this, please move to the step 3.)

You can download the dataset from http://www.cp.jku.at/datasets/Music4All-Onion/. The user-item interaction history comes in two formats:

 - Listening records (i.e. individual user-item interactions) with timestamp, or
 - Counts of interactions of a specific user with a specific item.

Additionally, there are files providing features for the tracks, that can be used for content-based recommendation.

Save the interaction history and content features you are going to use, in the current folder. For instance, for timestamp interactions
and the BoAW representation of chroma features, download `userid_trackid_timestamp.tsv` and `id_chroma_bow.tsv`. Then do:

```
bzip2 -dk userid_trackid_timestamp.tsv.bz2
bzip2 -dk id_chroma_bow.tsv.bz2
```

3.**Go the ``conversion_tools/`` directory 
and run the following command to get the atomic files of Music4All-Onion dataset.**

```
python run.py --dataset onion \
--input_path onion-data --output_path output_data/onion \
--interaction_type timestamp --convert_inter \
--convert_item --item_feature_name chroma_bow
```

`input_path` is the path of the input decompressed LFM-1b file.

`output_path` is the path to store converted atomic files.

`interaction_type` Onion user item interactions could be in timestamp or aggregated as counts.
 
`convert_inter` Pass this option to convert the user-item interaction to an '*.inter' atomic file.

`convert_item` Pass this option to convert the user-item interaction to an '*.item' atomic file.

`item_feature_name chroma_bow` is the name of the item feature to be converted.
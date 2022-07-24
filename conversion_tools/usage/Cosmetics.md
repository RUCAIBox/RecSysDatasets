# Cosmetics

1.**Clone the repository and install requirements.**
(If you have already done this, please move to the step 2.)

```sh
git clone https://github.com/RUCAIBox/RecDatasets
cd RecSysDatasets/conversion_tools
pip install -r requirements.txt
```

2.**Download the Cosmetics Dataset and extract the dataset file.**
(If you have already done this, please move to the step 3.)

* Create `cosmetics/`
* Download [eCommerce Events History in Cosmetics Shop](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop)
* Put it into `cosmetics/`
* Unzip it

```sh
mkdir cosmetics
# Download archive.zip
mv archive.zip ./cosmetics
unzip cosmetics/archive.zip -d cosmetics/
```

3.**Run the following command to get the atomic files of Cosmetics dataset.**

```sh
# cd RecSysDatasets/conversion_tools
python run.py --dataset cosmetics \
--input_path cosmetics --output_path cosmetics \
--convert_inter --convert_item
```

* `input_path` is the path of the input decompressed cosmetics file
* `output_path` is the path to store converted atomic files
* `convert_inter` Adult only can be converted to '*.inter' atomic file

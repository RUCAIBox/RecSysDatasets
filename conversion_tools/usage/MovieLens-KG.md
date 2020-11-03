# MovieLens - KG

Here we show how to generate the KG atomic files (*.kg and *.link)
for MovieLens dataset.

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the KG file from [Baidu Yun](https://pan.baidu.com/s/1p51sWMgVFbAaHQmL4aD_-g) or [Google Drive](https://drive.google.com/drive/folders/1so0lckI6N6_niVEYaBu-LIcpOdZf99kj?usp=sharing).**

The used KG file is in KGDatasets/, named MovieLens-KG.zip

```
unzip MovieLens-KG.zip -d MovieLens-KG
```

3.**Get the inter atomic file.**

You can refer to [MovieLens](https://github.com/RUCAIBox/RecDatasets/blob/master/conversion_tools/usage/MovieLens.md) 
to get the inter atomic file of MovieLens dataset,
such as 'ml-100k.inter', 'ml-1m.inter' and so on. 


4.**Go the ``conversion_tools/`` directory 
and run the following command to get the KG atomic files of MovieLens dataset.**

```
python add_knowledge.py --dataset ml-1m --inter_file ml-1m.inter \ 
--kg_data_path MovieLens-KG --output_path output_data/ml-1m/ --hop 1
```

After this, we will get 'ml-1m.kg' and 'ml-1m.link' in output_data/ml-1m/.

`dataset` is the dataset name, we will use this parameter to name the *.kg and *.link file

`inter_file` is the input inter file

`kg_data_path` is the path of MovieLens-KG obtained from Step 2

`output_path` is the path to store the converted kg atomic files

`hop` is the number of neighbor hops we generate for the items in knowledge graph. In our setting, the maximum is 3, default is 1.

**Notes:** You can change the relation by modifying MovieLens-KG/relation.kg. 
This can remove those useless relations and reduce the scale of the generated knowledge graph.
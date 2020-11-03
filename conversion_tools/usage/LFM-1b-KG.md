# LFM-1b - KG

Here we show how to generate the KG atomic files (*.kg and *.link)
for LFM-1b tracks dataset.

1.**Clone the repository and install requirements.** 
(If you have already done this, please move to the step 2.)

```
git clone https://github.com/RUCAIBox/RecDatasets

cd RecDatasets/conversion_tools

pip install -r requirements.txt
```

2.**Download the KG file from [Baidu Yun](https://pan.baidu.com/s/1p51sWMgVFbAaHQmL4aD_-g) or [Google Drive](https://drive.google.com/drive/folders/1so0lckI6N6_niVEYaBu-LIcpOdZf99kj?usp=sharing).**

The used KG file is in KGDatasets/, named LFM-1b-KG.zip

```
unzip LFM-1b-KG.zip -d LFM-1b-KG
```

3.**Get the inter atomic file**

You can refer to [LFM-1b](https://github.com/RUCAIBox/RecDatasets/blob/master/conversion_tools/usage/LFM-1b.md) 
to get the inter atomic file of LFM-1b dataset.

Only the lfm1b-tracks.inter can align to the KG we provided. 


4.**Go the ``conversion_tools/`` directory 
and run the following command to get the KG atomic files of LFM-1b dataset.**

```
python add_knowledge.py --dataset lfm1b-tracks --inter_file lfm1b-tracks.inter \ 
--kg_data_path LFM-1b-KG --output_path output_data/lfm1b-tracks/ --hop 1
```

After this, we will get 'lfm1b-tracks.kg' and 'lfm1b-tracks.link' in output_data/lfm1b-tracks/.

`dataset` is the dataset name, we will use this parameter to name the *.kg and *.link file

`inter_file` is the input inter file

`kg_data_path` is the path of LFM-1b-KG obtained from Step 2

`output_path` is the path to store the converted kg atomic files

`hop` is the number of neighbor hops we generate for the items in knowledge graph. In our setting, the maximum is 3, default is 1.

**Notes:** You can change the relation by modifying LFM-1b-KG/relation.kg. 
This can remove those useless relations and reduce the scale of the generated knowledge graph.
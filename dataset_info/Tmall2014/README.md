# Tmall2014

## Dataset Overview

Tmall2014 is a large-scale e-commerce dataset collected from Tmall.com (formerly Taobao Mall), containing user behavior logs from 2013. The dataset includes multiple types of user-item interactions: clicks, add-to-cart, favorites (collect), and purchases (alipay).

**For detailed dataset information, please visit:** [Tianchi Tmall Recommendation Dataset](https://tianchi.aliyun.com/dataset/140281)

## Data Format

The original data file uses `\x01` (ASCII control character) as field separator. After conversion, the data is in RecBole atomic file format (tab-separated):

```
user_id:token	item_id:token	timestamp:float
u6276408	3903192	1377496871
```

## Usage

Please refer to the [conversion tool documentation](../../conversion_tools/usage/Tmall2014.md) for instructions on how to convert this dataset to RecBole format.

# Taobao Dataset

## Dataset Information

**For detailed dataset information, please visit:** [Taobao User Behavior Dataset](https://tianchi.aliyun.com/dataset/dataDetail?dataId=649)

## Prerequisites

```bash
git clone https://github.com/RUCAIBox/RecDatasets
cd RecDatasets/conversion_tools
pip install -r requirements.txt
```

## Data Conversion

### Basic Usage

```bash
python run.py --dataset taobao \
  --input_path /path/to/Taobao.csv \
  --output_path output_data/taobao \
  --interaction_type pv \
  --convert_inter
```

### Parameters

- `--dataset`: `taobao` (required)
- `--input_path`: Path to the input data file (required)
- `--output_path`: Directory to store converted files (required)
- `--interaction_type`: `pv`, `cart`, `fav`, `buy`, or omit to merge all types (optional)
- `--convert_inter`: Enable conversion (required)
- `--duplicate_removal`: Enable deduplication (optional)

**Note**: When `--interaction_type` is omitted, all four interaction types (pv, cart, fav, buy) will be merged into a single file with an additional `action_type` column.

### Convert All Interaction Types

#### Method 1: Convert Separately
```bash
for type in pv cart fav buy; do
  python run.py --dataset taobao \
    --input_path /path/to/Taobao.csv \
    --output_path output_data/taobao \
    --interaction_type $type \
    --convert_inter
done
```

#### Method 2: Convert All Types in One File (Recommended)
```bash
python run.py --dataset taobao \
  --input_path /path/to/Taobao.csv \
  --output_path output_data/taobao \
  --convert_inter
```

## Output Format

### Single Interaction Type
Output file: `output_data/taobao/taobao-{interaction_type}/taobao-{interaction_type}.inter`

```
user_id:token	item_id:token	timestamp:float
1	2268318	1511544070
```

### All Interaction Types (Merged)
Output file: `output_data/taobao/taobao-merged/taobao-merged.inter`

```
user_id:token	item_id:token	timestamp:float	action_type:token
1	2268318	1511544070	pv
1	2268318	1511544071	cart
1	2268318	1511544072	fav
1	2268318	1511544073	buy
```

### With `--duplicate_removal`

#### Single Type:
```
user_id:token	item_id:token	timestamp:float	interactions:float
1	2268318	1511544070	3
```

#### Merged Types:
```
user_id:token	item_id:token	timestamp:float	action_type:token	interactions:float
1	2268318	1511544070	pv	1
1	2268318	1511544071	cart	2
```

## Dataset Statistics

- **Total interactions**: ~100 million
- **Behavior types**: pv (page view), cart (add to cart), fav (favorite), buy (purchase)
- **Time period**: 2017-11-25 to 2017-12-03
- **Users**: ~1 million
- **Items**: ~4 million

## Input Format

The input CSV file should have the following format:
```
user_id,item_id,category_id,behavior_type,timestamp
1,2268318,2520377,pv,1511544070
1,2333346,2520771,pv,1511561733
```

Where:
- `user_id`: User identifier
- `item_id`: Item identifier  
- `category_id`: Category identifier
- `behavior_type`: One of `pv`, `cart`, `fav`, `buy`
- `timestamp`: Unix timestamp

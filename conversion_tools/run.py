# @Time   : 2020/9/18
# @Author : Shanlei Mu
# @Email  : slmu@ruc.edu.cn


import argparse
import importlib
from conversion_tools.src import dataset2class


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='ml-1m')
    parser.add_argument('--input_path', type=str, default='../raw_data/ml-1m/')
    parser.add_argument('--output_path', type=str, default='../processed_data/ml-1m/')
    parser.add_argument('--merge_repeat', type=bool, default=False)
    args = parser.parse_args()

    dataset_class = getattr(importlib.import_module('extended_dataset'), dataset2class[args.dataset.lower()])
    c = dataset_class(args.input_path, args.output_path)
    c.convert_user()

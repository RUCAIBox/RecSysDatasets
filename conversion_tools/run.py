# @Time   : 2020/9/18
# @Author : Shanlei Mu
# @Email  : slmu@ruc.edu.cn


import argparse
import importlib

from src.utils import dataset2class


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='ml-1m')
    parser.add_argument('--input_path', type=str, default='../raw_data/ml-1m/')
    parser.add_argument('--output_path', type=str, default='../processed_data/ml-1m/')
    parser.add_argument('--interaction_type', type=str, default=None)
    parser.add_argument('--duplicate_removal', action='store_true')
    args = parser.parse_args()

    dataset_class = getattr(importlib.import_module('src.extended_dataset'), dataset2class[args.dataset.lower()])
    datasets = dataset_class(args.input_path, args.output_path, args.interaction_type, args.duplicate_removal)
    datasets.convert_inter()

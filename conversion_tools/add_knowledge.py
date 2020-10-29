# @Time   : 2020/10/29
# @Author : Shanlei Mu
# @Email  : slmu@ruc.edu.cn

import argparse

from src.kg_dataset import KGDataset


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='example')
    parser.add_argument('--inter_file', type=str, default=None)
    parser.add_argument('--kg_data_path', type=str, default=None)
    parser.add_argument('--output_path', type=str, default=None)
    parser.add_argument('--hop', type=int, default=1)
    args = parser.parse_args()

    assert args.inter_file is not None, 'inter_file can not be None'
    assert args.kg_data_path is not None, 'kg_data_path can not be None'
    assert args.output_path is not None, 'output_path can not be None'
    assert args.hop <= 3, 'hop must be less than 4'

    kg = KGDataset(args.dataset, args.inter_file, args.kg_data_path,
                   args.output_path, args.hop)
    kg.generate_link()
    kg.generate_knowledge()

# -*- coding: utf-8 -*-

import os
import logging
import numpy as np
import pandas as pd
from datetime import datetime

from src.base_dataset import BaseDataset


class CosmeticsDataset(BaseDataset):
    def __init__(self, input_path, output_path):
        super(CosmeticsDataset, self).__init__(input_path, output_path)
        self.dataset_name = "cosmetics"

        self.log = logging.getLogger(__file__)
        self.log.addHandler(logging.StreamHandler())
        self.log.setLevel(logging.INFO)

        self.sep = "\t"
        self.inter_fields = {
            "user_id":      "user_id:token",
            "product_id":   "item_id:token",
            "category_id":  "cate_id:token",
            "user_session": "sess_id:token",
            "event_type":   "event:token",
            "price":        "price:float",
            "event_time":   "timestamp:float"
        }

        if os.path.isfile(input_path):
            self.inter_file = [input_path]
        elif os.path.isdir(input_path):
            files = os.listdir(input_path)
            self.inter_file = [os.path.join(input_path, f).replace("\\", "/") for f in files if f.endswith(".csv")]
        else:
            self.log.error(f"Path not exists: {input_path}")
            exit(-1)

        self.output_inter_file = os.path.join(self.output_path, f"{self.dataset_name}.inter").replace("\\", "/")

    @staticmethod
    def _process_data(df):
        def process_row(et, us):
            # 2019-10-01 00:00:00 UTC
            ts = int(datetime.strptime(et.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S").timestamp())

            # 26dd6e6e-4dac-4778-8d2c-92e149dab885
            sess = str(us).replace("-", "")

            return ts, sess

        speedup = np.frompyfunc(process_row, 2, 2)

        return speedup(df["event_time"], df["user_session"])

    def convert_inter(self):
        df = pd.DataFrame()
        for f in self.inter_file:
            self.log.info(f"Reading {f}")
            df = pd.concat([df, pd.read_csv(f, usecols=self.inter_fields.keys())])

        self.log.info(f"Processing timestamp and user session")
        df["event_time"], df["user_session"] = self._process_data(df)
        df.rename(columns=self.inter_fields, inplace=True)

        self.log.info(f"Writing to file")
        df.to_csv(self.output_inter_file, sep=self.sep, index=False)

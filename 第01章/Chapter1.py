# -*-coding: utf-8 -*-
import numpy as np
import pandas as pd

if __name__ == "__main__":
    gaku = pd.read_csv('学力調査結果.csv', encoding = "shift-jis")
    print(gaku.describe())
# Description: This file is responsible
# for loading and presenting the data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pygame


class Data():
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(data_path)

    def load_data(self):
        return self.data

    def present_data(self):
        print(self.data.head())

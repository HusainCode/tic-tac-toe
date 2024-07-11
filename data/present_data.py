# Description: This file is responsible
# for loading and presenting the data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pygame


class PresentData():
    def __init__(self, data_path):
        self.data_path = data_path

    def present_data(self):
        print(self.data.head())

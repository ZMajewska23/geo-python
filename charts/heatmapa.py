import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from matplotlib.colors import Colormap, ListedColormap

def create_heatmap(df):
    df_hours_heatmap = df.groupby(by = ['godzina', 'data']).mean(numeric_only=True)['residua'].unstack()
    plot.figure(figsize = (10,7))
    sns.heatmap(df_hours_heatmap, cmap = 'coolwarm')
    plot.title("heatmap")
    plot.show()

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from matplotlib.colors import Colormap, ListedColormap
from scipy import signal
from os import path
 
def create_spectogram(df):
    for day in df['data'].unique():
        df_minutes_day = df[df['data'] == day]
    
        f, t, Sxx = signal.spectrogram(df_minutes_day['residua'], fs=1)
    
        plot.pcolormesh(t, f, Sxx, shading = 'gouraud')
        plot.ylim(0,0.01)
        plot.xlabel('Czas[min]')
        plot.ylabel('Residua [mGal]')
        plot.draw() 
        plot.show()

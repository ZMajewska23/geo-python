import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from matplotlib.colors import Colormap, ListedColormap
# from os import path
#outpath = r"C:\Users\user\Desktop\chyba_wazne\Zuza\python_kodzik\wykresy\polar_155"


def create_polar(df_hours):
    ticks = ['0h','1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h',
             '13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h']
    teta = np.deg2rad(np.arange(0,360,15))

    ax = plot.figure()
    ax = plot.subplot(111, projection='polar')

    for day in df_hours['data'].unique():
        df_hours_day = df_hours[df_hours['data'] == day]

        r_biegunowa=[]
        for i in df_hours_day['residua']:
            r_biegunowa.append(i)

        ax.set_xticks(np.linspace(0, 2*np.pi, 24, endpoint=False))
        ax.set_theta_zero_location('N', offset=0.0)
        ax.set_theta_direction(-1)
        ax.set_rlim(bottom=44500, top=45500)
        ax.set_xticklabels(ticks)
        plot.polar(teta, r_biegunowa)
        plot.show()
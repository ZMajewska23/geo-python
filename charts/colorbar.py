import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from matplotlib.colors import Colormap, ListedColormap
from os import path
#outpath = r"C:\Users\user\Desktop\chyba_wazne\Zuza\python_kodzik\wykresy\colorbar_155"

def create_colorbar(df_hours, liczbadni):
    for day in df_hours['data'].unique():
        df_hours_day = df_hours[df_hours['data'] == day]

        dwuwymiar = []  # Lista, która będzie przechowywać puste listy
        for i in range(24):
            new_list = []  # Tworzenie nowej pustej listy
            dwuwymiar.append(new_list)  # Dodawanie nowej pustej listy do listy lists
        q = 0
        qq = 0
        while q <= liczbadni-1:
            while qq <= 23:
                dwuwymiar[qq].append(df_hours['residua'][qq+q*24])
                qq += 1
            qq = 0
            q += 1

        cmap = plot.cm.jet
        cmap.set_bad(color='gray', alpha=0.3)
        plot.imshow(dwuwymiar, cmap='Blues', interpolation='none')
    plot.colorbar()
    plot.xlabel('Dzień')
    plot.ylabel('Godzina')
    plot.show()
import pandas as pd
from os import path
import numpy as np
import matplotlib.pyplot as plt

outpath = "C:/Users/user/Desktop/SEMI/kodzix/wykresy/periodogramy_RY"

def calculate_periodogram(data, fs):
    N = len(data)
    T = 1/fs
    yf = np.fft.fft(data)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    periodogram = (2.0/N) * np.abs(yf[0:N//2])
    return xf, periodogram

def create_periodogram(df):

    for day in df['data'].unique():
        df_seconds_day = df[df['data'] == day]


    # Wybierz kolumnę z danymi grawimetrycznymi
        gravity_data = df_seconds_day['residua']

    # Częstotliwość próbkowania (Hz)
        fs = 1 # Dla danych próbkowanych co sekunde

    # Oblicz periodogram
        xf, periodogram = calculate_periodogram(gravity_data, fs)

    # Wykres periodogramu
        plt.figure(figsize=(8, 4))
        plt.plot(xf, periodogram)
        plt.xlim(0,0.1)
        plt.ylim(0,50)
        plt.xlabel('Residua [mGal]')
        plt.ylabel('Widmowa gęstość mocy')
        plt.grid(True)
        plt.draw()
        plt.show()

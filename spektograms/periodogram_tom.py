import pandas as pd
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wczytanie_157 import df, df_minutes, df_hours, df_days, liczbadni, r
from scipy import signal

outpath = r"C:\Users\user\Desktop\chyba_wazne\Zuza\python_kodzik\wykresy\periodogramy_KA"

def calculate_periodogram(data, fs):
    N = len(data)
    T = 1/fs
    yf = np.fft.fft(data)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    periodogram = (2.0/N) * np.abs(yf[0:N//2])
    return xf, periodogram

# for day in df['data'].unique():
#     df_seconds_day = df[df['data'] == day]
# # Wybierz kolumnę z danymi grawimetrycznymi
#     gravity_data = df_seconds_day['residua[nm/s2]']
# # Częstotliwość próbkowania (Hz)
#     fs = 1 # Dla danych próbkowanych co sekunde
# # Oblicz periodogram
#     xf, periodogram = calculate_periodogram(gravity_data, fs)
# # Wykres periodogramu
#     plt.figure(figsize=(8, 4))
#     plt.plot(xf, periodogram)
#     plt.ylim(0,100)
#     plt.xlabel('Częstotliwość [Hz]')
#     plt.ylabel('Amplituda')
#     plt.title('Periodogram')
#     plt.grid(True)
#     plt.draw()
#     plt.savefig(path.join(outpath,"periodogram155_{0}.png".format(day)))
# #plt.show()

## PERIODOGRAM SIGNAL
for day in df['data'].unique():
    df_seconds_day = df[df['data'] == day]
# Wybierz kolumnę z danymi grawimetrycznymi
    gravity_data = df_seconds_day['residua[nm/s2]']
# Częstotliwość próbkowania (Hz)
    fs = 1 # Dla danych próbkowanych co sekunde
# Oblicz periodogram
    #xf, periodogram = calculate_periodogram(gravity_data, fs)

    f, Pxx_den = signal.periodogram(gravity_data, fs=1)
    plt.figure(figsize=(8, 4))
    plt.semilogy(f, Pxx_den)
    plt.xlim(0.002,0.5)
    plt.ylim(10**(-3),10**9)
    plt.xlabel('częstotliwość [Hz]')
    plt.ylabel('amplituda [m]')
    plt.draw()
    plt.savefig(path.join(outpath,"periodogram155_{0}.png".format(day)))

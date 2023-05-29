import os
import datetime
import pandas as pd
import numpy as np
from scipy import fft


def downoload_data_from_files(path, day_start, day_end):
    files = os.listdir(path)

    # jeżeli chcemy mieć wszystkie dane day_end podajemy None
    if day_end is None:
        day_end = len(files)

    files = files[day_start: day_end]
    df = pd.DataFrame()

    for file in files:
        nazwa = f'./data/gphone-155_2020/{file}'
        print(file)
        # pominięcie pierwszych linijek z metadanymi
        df_file = pd.read_csv(nazwa, sep='\t', skiprows=25)
        df_file = df_file['[DATA]'].str.split('  ', n=-1, expand=True)
        df_file.columns = ['data', 'godzina', 'raw[nm/s2]', 'ciśnienie[mBar]', 'residua[nm/s2]']
        df_file['godzina'] = df_file['godzina'].str.replace(" ", ":")

        df = pd.concat([df, df_file])

    # podział kolumn ogranicznikem '  '
    # df = df['[DATA]'].str.split('  ', n=-1, expand=True)
    # zdefiniowanie kolumn df
    df.columns = ['data', 'godzina', 'raw[nm/s2]', 'ciśnienie[mBar]', 'residua[nm/s2]']

    print('daty')
    # zamiana stringów danych na inny format
    df['data'] = pd.to_datetime(df['data'])
    # df['godzina'] = df['godzina'].str.replace(" ", ":")
    df['czas'] = df['data'] + pd.to_timedelta(df['godzina'])
    df['ciśnienie[mBar]'] = df['ciśnienie[mBar]'].astype(float)
    df['raw[nm/s2]'] = df['raw[nm/s2]'].astype(float)
    df['residua[nm/s2]'] = df['residua[nm/s2]'].astype(float)

    # usuwanie błędnych danych
    # df = df[(df['residua[nm/s2]'] > 0 )&(df['residua[nm/m2]'] > 0 )]
    df = df[(df['raw[nm/s2]'] != -9999)&(df['residua[nm/s2]'] != -9999)]

    print('wstawianie pustych')
    # tu wstawia NaN gdy nie ma pomiaru
    start = datetime.datetime.combine(df['czas'].min(), datetime.time.min)
    end = datetime.datetime.combine(df['czas'].max(), datetime.time.max)
    df_dates = _create_dates_df_from_row(start, end)
    df = pd.merge(df_dates, df, on='czas', how='outer')#.reset_index()

    print('daty v2')
    # tworzenie kolumn z czasem
    df['data'] = pd.to_datetime(df['czas'].dt.date)
    df['sekunda'] = pd.to_timedelta(df['godzina']).dt.seconds
    df['minuta'] = df['czas'].dt.minute
    df['godzina'] = df['czas'].dt.hour
    df['miesiac'] = df['czas'].dt.month
    df['rok'] = df['czas'].dt.year

    return df


# definicja funkcji tworzącej w miejscu braku danych w pliku wartości NaN
def _create_dates_df_from_row(date_start, date_end):
    df_dates = pd.DataFrame(
        {
            'czas': pd.date_range(date_start, date_end, freq='s', inclusive='left'),
        }
    )
    return df_dates


def create_grouped_df(df, grouped_columns, new_residua):
    # # średnie residua co minute
    df_grouped = df.groupby(grouped_columns).mean(numeric_only=True).reset_index()
    df_grouped.rename(columns={'residua[nm/s2]': new_residua}, inplace=True)

    return df_grouped

    # df_minutes = df.groupby(['data', 'godzina', 'minuta']).mean(numeric_only=True).reset_index()
    # df_minutes.rename(columns={'residua[nm/s2]': 'residua[nm/m2]'}, inplace=True)
    # df_minutes['czas'] = df_minutes['data'] + pd.to_timedelta(df_minutes['godzina'], 'hour') + pd.to_timedelta(df_minutes['minuta'], 'minute')
#
# # średnie residua co godzine
# df_hours = df.groupby(['data', 'godzina']).mean(numeric_only = True).reset_index()
# df_hours.rename(columns={'residua[nm/s2]': 'residua[nm/h]'}, inplace=True)
# df_hours['czas'] = df_hours['data'] + pd.to_timedelta(df_hours['godzina'], 'hour')
#
#
# # średnie residua z dni
# df_days = df.groupby(['data']).mean(numeric_only = True).reset_index()
# df_days.rename(columns={'residua[nm/s2]': 'residua[day]'}, inplace=True)
# df_days['czas'] = df_days['data']


# df_month = df.groupby(['miesiac', 'rok']).mean(numeric_only = True).reset_index()
# df_month.rename(columns={'residua[nm/s2]': 'residua[day]'}, inplace=True)
#
#
# ################################################################################
#
# liczba_probek = len(df['residua[nm/s2]'])
#
# # Przeliczenie jednostek przyspieszenia z nm/s^2 na mGal
# df['przyspieszenie'] = df['residua[nm/s2]'] / (10**4)
# przyspieszenie = df['przyspieszenie'].values
#
# # Obliczenie transformaty Fouriera
# transformaty = fft.fft(przyspieszenie)
#
# # Obliczenie wektora częstotliwości
# czestotliwosci = fft.fftfreq(liczba_probek, 1/84600)
#
# # Znalezienie indeksu maksymalnej amplitudy
# indeks_maks_amplitudy = np.argmax(np.abs(transformaty))
# print('%.10f', indeks_maks_amplitudy)
#
# # Obliczenie częstotliwości odpowiadającej maksymalnej amplitudzie
# czestotliwosc = czestotliwosci[indeks_maks_amplitudy]
# print(czestotliwosc)
#
# df['czestotliwosc[Hz]'] = np.abs(czestotliwosc)
# print('%.3f', df['czestotliwosc[Hz]'][100])

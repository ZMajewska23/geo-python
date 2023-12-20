import os
import datetime
import pandas as pd
import numpy as np
from scipy import fft


def download_data_from_files(path, day_start, day_end):
    files = os.listdir(path)

    # jeżeli chcemy mieć wszystkie dane day_end podajemy None
    if day_end is None:
        day_end = len(files)

    files = files[day_start: day_end]
    df = pd.DataFrame()

    for file in files:
        nazwa = f'{path}/{file}'
        print(file)
        # pominięcie pierwszych linijek z metadanymi
        df_file = pd.read_csv(nazwa, sep='\t', skiprows=25)
        df_file = df_file['[DATA]'].str.split('  ', n=-1, expand=True)
        df_file.columns = ['data', 'godzina', 'raw[nm/s2]', 'cisnienie[mBar]', 'residua']
        df_file['godzina'] = df_file['godzina'].str.replace(" ", ":")

        df = pd.concat([df, df_file])

    # podział kolumn ogranicznikem '  '
    # df = df['[DATA]'].str.split('  ', n=-1, expand=True)
    # zdefiniowanie kolumn df
    # df.columns = ['data', 'godzina', 'raw[nm/s2]', 'ciśnienie[mBar]', 'residua[nm/s2]']

    print('daty')
    # zamiana stringów danych na inny format
    df['data'] = pd.to_datetime(df['data'])
    df['czas'] = df['data'] + pd.to_timedelta(df['godzina'])
    df['cisnienie[mBar]'] = df['cisnienie[mBar]'].astype(float)
    df['raw[nm/s2]'] = df['raw[nm/s2]'].astype(float)
    df['residua'] = df['residua'].astype(float)

    # usuwanie błędnych danych
    df = df[(df['raw[nm/s2]'] != -9999)&(df['residua'] != -9999)]

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


def create_grouped_df(df, grouped_columns):
    # # średnie residua co minute
    df_grouped = df.groupby(grouped_columns).mean(numeric_only=True).reset_index()
    # df_grouped.rename(columns={'residua[nm/s2]': new_residua}, inplace=True)

    return df_grouped


def calculate_frequency(df):
    liczba_probek = len(df['residua'])

    # Przeliczenie jednostek przyspieszenia z nm/s^2 na mGal
    df['przyspieszenie'] = df['residua'] / (10**5)
    df['przyspieszenie']= np.log(df['przyspieszenie'])
    przyspieszenie = df['przyspieszenie'].values

    # Obliczenie transformaty Fouriera
    transformaty = fft.fft(przyspieszenie)

    # Obliczenie wektora częstotliwości
    czestotliwosci = fft.fftfreq(liczba_probek)

    df['czestotliwosc[Hz]'] = np.abs(czestotliwosci)
    # print('%.3f', df['czestotliwosc[Hz]'][100])

    return df

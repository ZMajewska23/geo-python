import pandas as pd
from download_data.wczytanie import download_data_from_files, create_grouped_df, calculate_frequency
from charts.spektogram import create_spectogram
from charts.periodogram import create_periodogram
from charts.heatmapa import create_heatmap
from charts.colorbar import create_colorbar
from charts.polar import create_polar
from charts.statystyki_def import*


path_155 = "./data/gphone-155_2020"

df = download_data_from_files(path_155, 332, 333)

df_minutes = create_grouped_df(df, ['data', 'godzina', 'minuta'])
df_minutes['czas'] = df_minutes['data'] + pd.to_timedelta(
    df_minutes['godzina'], 'hour') + pd.to_timedelta(df_minutes['minuta'], 'minute')

df_hours = create_grouped_df(df, ['data', 'godzina'])
df_hours['czas'] = df_hours['data'] + pd.to_timedelta(df_hours['godzina'], 'hour')

df_days = create_grouped_df(df, ['data'])
df_days['czas'] = df_days['data']

df_month = create_grouped_df(df, ['miesiac', 'rok'])


df.to_csv('data/df.csv', index=False)
df_minutes.to_csv('./data/df_minutes.csv', sep=';', decimal=',', index=False)
df_hours.to_csv('./data/df_hours.csv', index=False)
df_days.to_csv('./data/df_days.csv', index=False)
df_month.to_csv('./data/df_month.csv', index=False)

# create_spectogram(df_minutes)
create_periodogram(df)
# create_heatmap(df_minutes)
# create_colorbar(df_hours, 31)
# create_polar(df_hours)
# calculate_mean(df['miesiac'], df['przyspieszenie'])
# calculate_roll(df['miesiac'], df['przyspieszenie'])
# calculate_std(df['przyspieszenie'])
# calculate_var(df['przyspieszenie'])
# calculate_centr_std(df['residua'], df_minutes['residua'])
# calculate_corelation(df['residua'])
# calculate_quantile(df['residua'])
# calculate_body_mass(df['residua'])
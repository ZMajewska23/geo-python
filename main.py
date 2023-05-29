import pandas as pd
from download_data.wczytanie import downoload_data_from_files, create_grouped_df

path_155 = "./data/gphone-155_2020"

df = downoload_data_from_files(path_155, 0, None)

print('grupowanie')
df_minutes = create_grouped_df(df, ['data', 'godzina', 'minuta'], 'residua[nm/m2]')
df_minutes['czas'] = df_minutes['data'] + pd.to_timedelta(df_minutes['godzina'], 'hour') + pd.to_timedelta(df_minutes['minuta'], 'minute')


df_hours = create_grouped_df(df, ['data', 'godzina'], 'residua[nm/h]')
df_hours['czas'] = df_hours['data'] + pd.to_timedelta(df_hours['godzina'], 'hour')

df_days = create_grouped_df(df, ['data'], 'residua[day]')
df_days['czas'] = df_days['data']

df_month = create_grouped_df(df, ['miesiac', 'rok'], 'residua[month]')

df_minutes.to_csv('df_minutes.csv', index=False)
df_hours.to_csv('df_hours.csv', index=False)
df_days.to_csv('df_days.csv', index=False)
df_month.to_csv('df_month.csv', index=False)


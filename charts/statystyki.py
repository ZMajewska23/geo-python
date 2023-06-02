import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import statsmodels as sm


########wczytanie csv
df_month = pd.read_csv('data/df_month.csv', sep=';', decimal=',')

##########caluclate_mean
# srednie = df_month.groupby(['miesiac', 'rok']).mean(numeric_only=True).reset_index()

# # print(srednie)
###############
# srednie = df_month['czestotliwosc[Hz]'].mean()
# print(srednie)

# plot.figure(figsize = (6,3))
# plot.scatter(df_month['miesiac'], df_month['czestotliwosc[Hz]'])
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()

##########średnia krocząca
step_mean = df_month['residua'].rolling(window=7, step = None)
# print(step_mean.min())


# plot.figure(figsize = (7,5))
# plot.scatter(df_month['miesiac'], df_month['residua'])
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()

##############
#wczytanie csv
df_days = pd.read_csv('data/df_days.csv', sep=';', decimal=',')
#wczytanie csv
df_hours = pd.read_csv('data/df_hours.csv', sep=';', decimal=',')
#wczytanie csv
df_minutes = pd.read_csv('data/df_minutes.csv', sep=';', decimal=',')
#wczytanie csv
df = pd.read_csv('data/df.csv', sep=';', decimal=',')


##########mediana
median = df_month.groupby(['miesiac', 'rok']).median(numeric_only=True).reset_index()

# print(median)

# plot.figure(figsize = (7,5))
# plot.scatter(df_month['miesiac'], df_month['przyspieszenie'])
# #plot.plot(df_month['residua'])
# plot.xlabel('Months')
# plot.ylabel('Residua')
# plot.title("Rozkład mediany według godzin w ciągu roku")
# plot.show()


##########odchylenie_standardowe
std = df_month.groupby('miesiac')['czestotliwosc[Hz]'].std()

# plot.figure(figsize = (7,5))
# #plot.plot(df_month['czestotliwosc[Hz]'])
# plot.scatter(df_month['miesiac'], df_month['czestotliwosc[Hz]'])
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład odchylenia standardowego na przestrzeni miesięcy")
# plot.show()

##########wariancja
var = df_month.groupby('miesiac')['czestotliwosc[Hz]'].var()

# plot.figure(figsize = (7,5))
# #plot.plot(df_month['czestotliwosc[Hz]'])
# plot.scatter(df_month['miesiac'], df_month['czestotliwosc[Hz]'])
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład wariancji częstotliwości na przestrzeni miesięcy")
# plot.show()

########odchylenie_centralne
# std2 = df_month.groupby('miesiac')['czestotliwosc[Hz]'].std()
# mean2 = df_month.groupby(['miesiac'], ['rok']).mean(numeric_only=True)

# stdc = mean2 - std2
# print(stdc)

# plot.figure(figsize = (10,7))
# plot.plot(stdc)
# plot.xlabel('Months')
# plot.ylabel('Przyspieszenie')
# plot.title("Rozkład odchylenia standardowego na przestrzeni miesięcy")
# plot.show()


##########quantils
q = df_month.groupby(['miesiac', 'rok']).quantile(q=0.25)

# plot.figure(figsize = (7,5))
# #plot.plot(df_month['czestotliwosc[Hz]'])
# plot.scatter(df_month['miesiac'], q)
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("\kwantyle częstotliwości na przestrzeni miesięcy")
# plot.show()

##########corelation
cor = df_month.groupby(['miesiac', 'rok']).mean(numeric_only=True).reset_index()

# plot.figure(figsize = (7,5))
# #plot.plot(df_month['czestotliwosc[Hz]'])
# plot.scatter(df_month['miesiac'], q)
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("\kwantyle częstotliwości na przestrzeni miesięcy")
# plot.show()

df_month['residua'].corr(method='spearman')
plot.figure(figsize = (10,7))
plot.plot(df['residua'])
plot.xlabel('Months')
plot.ylabel('Przyspieszenie')
plot.title("Korelacja metodą rang Spearmana")
plot.show()
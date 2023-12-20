import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import statsmodels as sm
import csv

#wczytanie csv dla miesiecy
df_month = pd.read_csv('data/df_month_r.csv', sep=';', decimal=',')
#wczytanie csv dla dni
df_days = pd.read_csv('data/df_days_r.csv', sep=';', decimal=',')
#wczytanie csv dla godzin
df_hours = pd.read_csv('data/df_hours_r.csv', sep=';', decimal=',')
#wczytanie csv dla minut
df_minutes = pd.read_csv('data/df_minutes_r.csv', sep=';', decimal=',')

#analiza wstepna
# df_stats = df_minutes.describe()
# print(df_stats)
# df_stats = df_hours.describe()
# print(df_stats)
# df_stats = df_days.describe()
# print(df_stats)
# df_stats = df_month.describe()
# print(df_stats)

# print(min(df_month['przyspieszenie']))
# print(max(df_month['przyspieszenie']))

#####SREDNIA

#srednia dla dni 
# df_mean = df_days.groupby(['data']).mean(numeric_only=True).reset_index()
# print("dzień ze średnią maksymalną:", df_mean.max())
# print("dzień ze średnią minimalną:", df_mean.min())

# print(max(df_mean['przyspieszenie']))
# print(min(df_mean['przyspieszenie']))

# srednia_miesiac = df_mean['przyspieszenie'].to_string(header=False, index=False)
# with open('srednia_miesiac.txt', 'w') as f:
#     f.write(srednia_miesiac)

###WYKRES ZE ŚREDNIĄ
# plot.figure(figsize = (6,3))
# plot.scatter(df_month['miesiac'], df_month['przyspieszenie'])
# plot.xlabel('Miesiac')
# plot.ylabel('Przyspieszenie')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()

# plot.figure(figsize = (20,3))
# plot.scatter(df_days['data'], df_days['przyspieszenie'])
# plot.xlabel('Dzień')
# plot.ylabel('Przyspieszenie')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()

###########średnia krocząca
# df_step_mean = df_month['przyspieszenie'].rolling(window=3, step = None)
# print("średnią minimalną wg miesiecy:", df_step_mean.min())
# print("średnia maksymalną wg miesiecy:", df_step_mean.max())

# ####WYKRES ZE ŚREDNIĄ KROCZĄCĄ
# plot.figure(figsize = (7,5))
# plot.scatter(df_month['miesiac'], df_step_mean.min())
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()
# Wczytaj istniejący plik CSV
# with open('data/df_month_step.csv', 'r') as file:
#     lines = file.readlines()

# df_month_step = pd.read_csv('data/df_month_step.csv', sep=';', decimal=',')
# string = df_month_step['miesiac'].to_string(index=False)

# miesiace = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

# df_step = pd.DataFrame({'data': miesiace, 'średnia krocząca': df_step_mean, 'przyspieszenie': df_month_step['przyspieszenie']})
# sns.lineplot( x='data', y='przyspieszenie', label='pomiar grawimetryczny')
# sns.lineplot( x='data', y='średnia krocząca', label='średnia krocząca miesięcy')
# plot.xlabel('data')
# plot.ylabel('przyspieszenie')
# plot.legend()
# plot.show()

# # Nie można użyć writer jako DataFrame, musisz użyć wcześniej utworzonych danych
# df_month['data'] = [row[0] for row in lines]  # Przyjmuję, że dane, które chcesz umieścić w kolumnie 'data', są w pierwszej kolumnie w lines

# df_step = pd.DataFrame({'data': df_month['data'], 'średnia krocząca': df_step_mean, 'przyspieszenie': [row[1] for row in lines]})  # Zmieniłem 'writer['przyspieszenie']' na [row[1] for row in lines]
# sns.lineplot(x='data', y='przyspieszenie', data=df_step, label='pomiar grawimetryczny')
# sns.lineplot(x='data', y='średnia krocząca', data=df_step, label='średnia krocząca miesięcy')
# plot.xlabel('data')
# plot.ylabel('przyspieszenie')
# plot.legend()
# plot.show()

##########mediana
#df_median = df_days.groupby(['data', 'godzina']).median(numeric_only=True).reset_index()
# print(df_median)
# print('mediana max', max(df_median['przyspieszenie']))
# print('mediana min', min(df_median['przyspieszenie']))

# df_days['data'] = pd.to_datetime(df_days['data'],format='%Y-%m-%d')
# mediany_przyspieszenia = df_days.groupby(df_days['data'].dt.month)['przyspieszenie'].median()

# ktorymiesiac = 1
# dane_mediany = []
# while ktorymiesiac < 13:
#     dane_mediany.append(mediany_przyspieszenia[ktorymiesiac])
#     ktorymiesiac += 1
# print(dane_mediany)
# listamiesiecy = [i for i in range(1, 13)]

# plot.figure(figsize = (6,3))
# plot.scatter(listamiesiecy, dane_mediany)
# plot.xlabel('Miesiac')
# plot.ylabel('Przyspieszenie')
# plot.title("Rozkład median miesięcznych")
# plot.show()

'''
###WYKRES DLA MEDIANY
plot.figure(figsize = (10,6))
plot.scatter(df_median['data'], df_median['przyspieszenie'])
#plot.plot(df_month['residua'])
plot.gca().xaxis.set_major_locator(plot.MaxNLocator(14))
plot.xticks(rotation=45, fontweight='light',  fontsize='x-small',)
plot.xlabel('Miesiac')
plot.ylabel('Residua')
plot.title("Rozkład mediany według dni w ciągu roku")
plot.show()
'''


##########kwantyle
q25 = df_month.quantile(q=0.25, interpolation='nearest', numeric_only=True)
print("Wyniki w pierwszym kwartylu:", q25)
q50 = df_month.quantile(q=0.50, interpolation='nearest', numeric_only=True)
print("Wyniki w drugim kwartylu:", q50)
q75 = df_month.quantile(q=0.75, interpolation='nearest', numeric_only=True)
print("Wyniki w trzecim kwartylu:", q75)

# q25 = df_month.quantile(q=0.25, interpolation='higher', numeric_only=True)
# print("Wyniki w pierwszym kwartylu:", q25)
# q50 = df_month.quantile(q=0.50, interpolation='higher', numeric_only=True)
# print("Wyniki w drugim kwartylu:", q50)
# q75 = df_month.quantile(q=0.75, interpolation='higher', numeric_only=True)
# print("Wyniki w trzecim kwartylu:", q75)

# q25 = df_month.quantile(q=0.25, interpolation='lower', numeric_only=True)
# print("Wyniki w pierwszym kwartylu:", q25)
# q50 = df_month.quantile(q=0.50, interpolation='lower', numeric_only=True)
# print("Wyniki w drugim kwartylu:", q50)
# q75 = df_month.quantile(q=0.75, interpolation='lower', numeric_only=True)
# print("Wyniki w trzecim kwartylu:", q75)


###WYKRESY DO KWANTYLI??
grupa = {'I': df_month['przyspieszenie'][:4],
'II': df_month['przyspieszenie'][5:8],
'III': df_month['przyspieszenie'][9:12]}

# sns.violinplot(data=df_month, x=df_month['przyspieszenie'], y=grupa)
sns.violinplot(data=pd.DataFrame(grupa))
plot.xlabel('Kwartyle')
plot.ylabel('Przyspieszenie')
plot.title('Rozkład przyspieszenia w kwartylach')
plot.show()

##########odchylenie_standardowe
'''
# std_month = df_month['przyspieszenie'].std()
# std_day = df_days['przyspieszenie'].std()
# std_hours = df_hours['przyspieszenie'].std()
# # print('odchylenie standardowe', std_month)

# data = [std_month, std_day, std_hours]
# plot.bar(np.arange(len(data)), data)
# plot.xticks(np.arange(len(data)),['miesięczne', 'dzienne', 'godzinne'])
# plot.title('Odchylenia standardowe')
# plot.ylim(0,1.75)
# plot.show()
'''

std_month = df_month['przyspieszenie'].std()
std_day = df_days['przyspieszenie'].std()
std_hours = df_hours['przyspieszenie'].std()
print('odchylenie standardowe', std_month)

plot.figure(figsize = (4,3))
plot.scatter(1, std_month, color='red', s = 150, label='miesięczne')
plot.scatter(2, std_day, color='green', s = 150, label='dzienne')
plot.scatter(3, std_hours, color='blue', s = 150, label='godzinne')
plot.xticks([])
plot.title('Odchylenia standardowe')
plot.legend(loc = 'lower right')
plot.show()




##########wariancja
var_month = df_month['przyspieszenie'].var()
var_day = df_days['przyspieszenie'].var()
var_hours = df_hours['przyspieszenie'].var()
print('wariancja', var_month)

#######odchylenie_centralne
std2 = df_month['przyspieszenie'].std()
mean2 = df_month['przyspieszenie'].mean()

stdc = mean2 - std2
print('odchylenie centralne', stdc)

#########KORELACJA
# cor = df_month[['miesiac', 'raw[nm/s2]', 'cisnienie[mBar]', 'residua', 'przyspieszenie', 'czestotliwosc[Hz]']].corr()
# print('korelacja', cor)
# save_string = cor.to_string(header=False, index=False)

# with open('korelacja.txt', 'w') as f:
#     f.write(save_string)

# data = np.array([df_days['przyspieszenie'],
#                  df_days['czestotliwosc[Hz]']])
# correlation_matrix = np.corrcoef(data)
# print(correlation_matrix)
# plot.imshow(correlation_matrix, cmap='RdBu', vmin=-1, vmax=1)
# plot.colorbar()
# plot.title('Wykres korelacji')
# plot.xticks([0, 1], ['g', 'Hz'])
# plot.yticks([0, 1], ['g', 'Hz'])
# plot.show()

# sns.heatmap(df_minutes[['przyspieszenie', 'czestotliwosc[Hz]']].corr(), cmap='coolwarm', annot=True)
# plot.show()
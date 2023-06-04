import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import statsmodels as sm

#wczytanie csv dla miesiecy
df_month = pd.read_csv('data/df_month.csv', sep=';', decimal=',')
#wczytanie csv dla dni
df_days = pd.read_csv('data/df_days.csv', sep=';', decimal=',')
#wczytanie csv dla godzin
df_hours = pd.read_csv('data/df_hours.csv', sep=';', decimal=',')
#wczytanie csv dla minut
df_minutes = pd.read_csv('data/df_minutes.csv', sep=';', decimal=',')

#analiza wstepna
# df_stats = df_minutes.describe()
# print(df_stats)
# df_stats = df_hours.describe()
# print(df_stats)
# df_stats = df_days.describe()
# print(df_stats)
df_stats = df_month.describe()
# print(df_stats)


#####SREDNIA

#srednia dla dni 
# df_mean = df_days.groupby(['data']).mean(numeric_only=True).reset_index()
# print("dzień ze średnią maksymalną:", df_mean.max())
# print("dzień ze średnią minimalną:", df_mean.min())

###WYKRES ZE ŚREDNIĄ
# plot.figure(figsize = (6,3))
# plot.scatter(df_month['miesiac'], df_month['czestotliwosc[Hz]'])
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()

############średnia krocząca
df_step_mean = df_month['czestotliwosc[Hz]'].rolling(window=1, step = None)
# print("średnią minimalną wg miesiecy:", df_step_mean.min())
# print("średnia maksymalną wg miesiecy:", df_step_mean.max())

####WYKRES ZE ŚREDNIĄ KROCZĄCĄ
# plot.figure(figsize = (7,5))
# plot.scatter(df_month['miesiac'], df_step_mean.min())
# plot.xlabel('Months')
# plot.ylabel('Frequency')
# plot.title("Rozkład średnich miesięcznych")
# plot.show()

##########mediana
df_median = df_days.groupby(['data']).median(numeric_only=True).reset_index()
# print(min(df_median['przyspieszenie']))


###WYKRES DLA MEDIANY
# plot.figure(figsize = (15,6))
# plot.scatter(df_median['data'], df_median['przyspieszenie'])
# #plot.plot(df_month['residua'])
# plot.xlabel('Months')
# plot.ylabel('Residua')
# plot.title("Rozkład mediany według dni w ciągu roku")
# plot.show()


##########kwantyle
# q25 = df_month.quantile(q=0.25, interpolation='nearest', numeric_only=True)
# print("Wyniki w pierwszym kwartylu:", q25)
# q50 = df_month.quantile(q=0.50, interpolation='nearest', numeric_only=True)
# print("Wyniki w drugim kwartylu:", q50)
# q75 = df_month.quantile(q=0.75, interpolation='nearest', numeric_only=True)
# print("Wyniki w trzecim kwartylu:", q75)

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
#sns.lmplot(x="przyspieszenie", y="liczba", hue="smoker", col="time", data=df_month);

##########odchylenie_standardowe
# std = df_month.std()
# print(std)

##########wariancja
# var = df_month.var()
# print(var)

########odchylenie_centralne
std2 = df_month['przyspieszenie'].std()
mean2 = df_month['przyspieszenie'].mean()

stdc = mean2 - std2
# print(stdc)

#########KORELACJA
cor = df_month[['miesiac', 'raw[nm/s2]', 'cisnienie[mBar]', 'residua', 'przyspieszenie', 'czestotliwosc[Hz]']].corr()
# print(cor)
save_string = cor.to_string(header=False, index=False)

# with open('korelacja.txt', 'w') as f:
#     f.write(save_string)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import statsmodels as sm

def calculate_mean(t,df):
    t = df['miesiac']
    srednia = df['czestotliwosc[Hz]'].mean()
    plot.figure(figsize = (10,7))
    plot.scatter(t, srednia)
    plot.xlabel('Months')
    plot.ylabel('Częstotliwość')
    plot.title("Rozkład średnich miesięcznych")
    plot.show()

def calculate_roll(t,df):
    t = df['miesiac']
    srednia = df['czestotliwosc[Hz]'].rolling(window=7, step = None)
    plot.figure(figsize = (10,7))
    plot.scatter(t, srednia)
    plot.xlabel('Months')
    plot.ylabel('Częstotliwość')
    plot.title("Rozkład średnich miesięcznych")
    plot.show()


def calculate_std(df):
    df['residua'].set_index('miesiac').std()
    plot.figure(figsize = (10,7))
    plot.plot(df['residua'])
    plot.xlabel('Months')
    plot.ylabel('Przyspieszenie')
    plot.title("Rozkład odchylenia standardowego na przestrzeni miesięcy")
    plot.show()


def calculate_var(df):
    df['czestotliwosc[Hz]'].set_index('miesiac').var()
    plot.figure(figsize = (10,7))
    plot.plot(df['czestotliwosc[Hz]'])
    plot.xlabel('Months')
    plot.ylabel('Częstotliwość')
    plot.title("Rozkład wariancji częstotliwości na przestrzeni miesięcy")
    plot.show()


def calculate_centr_std(df, df_minutes):
    df['residua'].set_index('miesiac').std() - df_minutes['residua'].mean()
    plot.figure(figsize = (10,7))
    plot.plot(df['residua'])
    plot.xlabel('Months')
    plot.ylabel('Przyspieszenie')
    plot.title("Rozkład odchylenia standardowego na przestrzeni miesięcy")
    plot.show()


def calculate_corelation(df):
    df['residua'].corr(method='spearman')
    plot.figure(figsize = (10,7))
    plot.plot(df['residua'])
    plot.xlabel('Months')
    plot.ylabel('Przyspieszenie')
    plot.title("Korelacja metodą rang Spearmana")
    plot.show()


def calculate_quantile(df):
    df['residua'].quantile(q=0.25)
    plot.figure(figsize = (10,7))
    plot.plot(df['residua'])
    plot.xlabel('Months')
    plot.ylabel('Przyspieszenie')
    plot.title("Rozkład wartości przyspieszenia w kwantylach")
    plot.show()

def calculate_body_mass(df):
    sns.set_theme(style="ticks")
    df = sns.load_dataset("penguins")
    sns.pairplot(df, hue="species")
    
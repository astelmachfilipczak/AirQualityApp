import sqlite3
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# wykonanie zapytania SQL:
cursor.execute('SELECT * FROM measurements')

# pobranie wyników zapytania:
data = cursor.fetchall()

print(data)

df = pd.DataFrame(data)
print(df)

# największa wartość
max_value = df[1].max()

# najmniejsza wartość
min_value = df[1].min()

# kiedy wartości wystąpiły
min_date = df.loc[df[1].idxmin(), 0]
max_date = df.loc[df[1].idxmax(), 0]

#średnia
data_mean = df[1].mean()

# zamknięcie połączenia
conn.close()

# wyświetlenie wyników
print("Najmniejsza wartość: ", min_value)
print("Data dla wartości najmniejszej: ", min_date)
print("Największa wartość: ", max_value)
print("Data dla wartości największej: ", max_date)
print("Średnia to: ", data_mean)

######TREND
# 1. ŚREDNIA KROCZĄCA
# oblicz średnią kroczącą z oknem ruchomym 30 dni
window_size = 30
trend = df[1].rolling(window=window_size).mean()
# wykres danych i trendu
plt.title('Metoda średniej kroczącej')
plt.plot(df[0], df[1], label='Dane')
plt.plot(df[0], trend, label='Trend')
plt.legend()
plt.show()

# 2. DOPASOWANIE KRZYWEJ REGRESJI
# dopasuj krzywą regresji do danych
x = np.arange(len(df))
p = np.polyfit(x, df[1], 1)

# wykres danych i krzywej regresji
plt.title('Metoda dopasowania krzywej regresji')
plt.plot(df[0], df[1], label='Dane')
plt.plot(df[0], p[0]*x + p[1], label='Trend')
plt.legend()
plt.show()

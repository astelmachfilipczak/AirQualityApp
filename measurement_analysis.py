import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


class MeasurementAnalysis:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_data(self):
        self.cursor.execute('SELECT * FROM measurements')
        data = self.cursor.fetchall()
        df = pd.DataFrame(data)
        df[0] = pd.to_datetime(df[0])
        df[1] = pd.to_numeric(df[1])
        return df

    def chart(self):
        df = self.get_data()
        plt.figure(figsize=(14, 7))
        plt.grid(True, which='both')
        plt.title('Wyniki pomiarów')
        plt.xlabel('Data pomiaru')
        plt.xticks(rotation=90)
        plt.ylabel('Wartości pomiarowe')
        plt.plot(df[0], df[1], label='Dane')
        plt.legend()
        plt.show()

    def analyze(self):
        df = self.get_data()
        plt.figure(figsize=(14, 7))
        max_value = df[1].max()
        min_value = df[1].min()
        min_date = df.loc[df[1].idxmin(), 0]
        max_date = df.loc[df[1].idxmax(), 0]
        data_mean = df[1].mean()
        window_size = 30
        trend = df[1].rolling(window=window_size).mean()
        plt.title('Metoda średniej kroczącej')
        plt.plot(df[0], df[1], label='Dane')
        plt.plot(df[0], trend, label='Trend')
        plt.legend()
        plt.show()
        self.conn.close()
        return {'max_value': max_value,
                'min_value': min_value,
                'min_date': min_date,
                'max_date': max_date,
                'data_mean': data_mean}







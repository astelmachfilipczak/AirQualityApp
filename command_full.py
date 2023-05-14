from get_stations_data import get_stations_data
from get_sensors_data import get_sensors_data
from get_measurements_data import get_measurements_data
from tkinter import *
import tkinter as tk
import sqlite3
from measurement_analysis import MeasurementAnalysis
from print_analysis import AnalysisWindow

def command_full():
    """
        Funkcja wyświetla listę wszytskich stacji pomiarowych i umożliwia przeglądanie w oknie.

        """

    def show_measurements_data():
        # usunięcie zawartości listboxa:
        listbox.delete(0, END)

        # Pobieranie danych pomiarowych wybranego stanowiska:
        id = int(entry_id.get())
        get_measurements_data(id)

        # wykonanie zapytania SQL:
        cursor.execute('SELECT * FROM measurements')

        # pobranie wyników zapytania:
        result3 = cursor.fetchall()

        # dodanie wyników zapytania do listboxa:
        for row in result3:
            listbox.insert(tk.END, row)

        MeasurementAnalysis('database.db').chart()

    def show_sensors_data():
        # usunięcie zawartości listboxa:
        listbox.delete(0, END)

        # Pobieranie danych odnośnie stanowisk pomiarowych dla wybranej stacji:
        stationId = int(entry_staionId.get())
        get_sensors_data(stationId)

        # wykonanie zapytania SQL:
        cursor.execute('SELECT * FROM sensors')

        # pobranie wyników zapytania:
        result = cursor.fetchall()

        # dodanie wyników zapytania do listboxa:
        for row in result:
            listbox.insert(tk.END, row)

    # Utworzenie okna i wyznaczenie jego rozmiaru:
    root = tk.Tk()
    root.title("AirQualityApp")
    root.geometry('1200x700')

    tk.Label(root, text="---Pełna lista stacji pomiarowych---").pack()
    tk.Label(root, text="").pack()

    # Utworzenie ramki:
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=NO)

    # # Utworzenie listboxa:
    listbox = Listbox(root)
    listbox.pack(side=TOP, fill=BOTH, expand=YES)

    # Utworzenie suwaka i przypisanie go do listboxa:
    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # wprowadzamy elementy interfejsu:
    label_staionId = Label(frame, text="PODAJ ID STACJI W CELU WYŚWIETLENIA STANOWISK POMIAROWYCH")
    label_id = Label(frame, text="PODAJ ID STANOWISKA W CELU WYŚWIETLENIA DANYCH POMIAROWYCH")
    label_analysis = Label(frame, text="DOKONAJ ANALIZY DANYCH")

    entry_staionId = Entry(frame, bd=5)
    entry_id = Entry(frame, bd=5)

    button_stationId = Button(frame, text="Szukaj", command=show_sensors_data)
    button_id = Button(frame, text="Szukaj", command=show_measurements_data)
    button_analysis = Button(frame, text="Analiza danych", command=AnalysisWindow)

    # rozmieszczenie elementów:
    label_staionId.grid(row=1, column=0, padx=10)
    label_id.grid(row=2, column=0, padx=10)
    label_analysis.grid(row=3, column=0, padx=10)

    entry_staionId.grid(row=1, column=1, padx=10)
    entry_id.grid(row=2, column=1, padx=10)

    button_stationId.grid(row=1, column=2, padx=10)
    button_id.grid(row=2, column=2, padx=10)
    button_analysis.grid(row=3, column=1, padx=10)

    # Wywołanie funkcji w celu zapisu w bazie danych:
    get_stations_data()

    # utworzenie połączenia z bazą danych:
    conn = sqlite3.connect('database.db')

    # utworzenie kursora:
    cursor = conn.cursor()

    # wykonanie zapytania SQL
    cursor.execute('SELECT * FROM stations')

    # pobranie wyników zapytania:
    result = cursor.fetchall()

    # dodanie wyników zapytania do listboxa:
    for row in result:
        listbox.insert(tk.END, row)

    root.mainloop()

if __name__ == '__main__': command_full()

#
# class CommandFull(Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("AirQualityApp")
#         self.geometry('1200x700')
#
#         tk.Label(self, text="---Pełna lista stacji pomiarowych---").pack()
#         tk.Label(self, text="").pack()
#
#         # Utworzenie ramki:
#         self.frame = Frame(self)
#         self.frame.pack(fill=BOTH, expand=NO)
#
#         # Utworzenie listboxa:
#         self.listbox = Listbox(self)
#         self.listbox.pack(side=TOP, fill=BOTH, expand=YES)
#
#         # Utworzenie suwaka i przypisanie go do listboxa:
#         scrollbar = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
#         self.listbox.config(yscrollcommand=scrollbar.set)
#         scrollbar.pack(side=RIGHT, fill=Y)
#
#         # wprowadzamy elementy interfejsu:
#         self.label_staionId = Label(self.frame, text="PODAJ ID STACJI W CELU WYŚWIETLENIA STANOWISK POMIAROWYCH")
#         self.label_id = Label(self.frame, text="PODAJ ID STANOWISKA W CELU WYŚWIETLENIA DANYCH POMIAROWYCH")
#         self.label_analysis = Label(self.frame, text="DOKONAJ ANALIZY DANYCH")
#
#         self.entry_staionId = Entry(self.frame, bd=5)
#         self.entry_id = Entry(self.frame, bd=5)
#
#         self.button_stationId = Button(self.frame, text="Szukaj", command=self.show_sensors_data)
#         self.button_id = Button(self.frame, text="Szukaj", command=self.show_measurements_data)
#         self.button_analysis = Button(self.frame, text="Analiza danych", command=AnalysisWindow)
#
#         # rozmieszczenie elementów:
#         self.label_staionId.grid(row=1, column=0, padx=10)
#         self.label_id.grid(row=2, column=0, padx=10)
#         self.label_analysis.grid(row=3, column=0, padx=10)
#
#         self.entry_staionId.grid(row=1, column=1, padx=10)
#         self.entry_id.grid(row=2, column=1, padx=10)
#
#         self.button_stationId.grid(row=1, column=2, padx=10)
#         self.button_id.grid(row=2, column=2, padx=10)
#         self.button_analysis.grid(row=3, column=1, padx=10)
#
#         # Wywołanie funkcji w celu zapisu w bazie danych:
#         get_stations_data()
#
#         # utworzenie połączenia z bazą danych:
#         self.conn = sqlite3.connect('database.db')
#
#         # utworzenie kursora:
#         cursor = self.conn.cursor()
#
#         # wykonanie zapytania SQL
#         cursor.execute('SELECT * FROM stations')
#
#         # pobranie wyników zapytania:
#         result = cursor.fetchall()
#
#         # dodanie wyników zapytania do listboxa:
#         for row in result:
#             self.listbox.insert(tk.END, row)
#
#         self.mainloop()
#
#     def show_measurements_data(self):
#         # usunięcie zawartości listboxa:
#         self.listbox.delete(0, tk.END)
#
#         # Pobieranie danych pomiarowych wybranego stanowiska:
#         id = int(self.entry_id.get())
#         get_measurements_data(id)
#
#         # wykonanie zapytania SQL:
#         # utworzenie kursora:
#         cursor = self.conn.cursor()
#         cursor.execute('SELECT * FROM measurements')
#
#         # pobranie wyników zapytania:
#         result = cursor.fetchall()
#
#         # dodanie wyników zapytania do listboxa:
#         for row in result:
#             self.listbox.insert(tk.END, row)
#
#         MeasurementAnalysis('database.db').chart()
#
#     def show_sensors_data(self):
#         # usunięcie zawartości listboxa:
#         self.listbox.delete(0, END)
#
#         # Pobieranie danych odnośnie stanowisk pomiarowych dla wybranej stacji:
#         stationId = int(self.entry_staionId.get())
#         get_sensors_data(stationId)
#
#         # wykonanie zapytania SQL:
#         # utworzenie kursora:
#         cursor = self.conn.cursor()
#         cursor.execute('SELECT * FROM sensors')
#
#         # pobranie wyników zapytania:
#         result = cursor.fetchall()
#
#         # dodanie wyników zapytania do listboxa:
#         for row in result:
#             self.listbox.insert(tk.END, row)
#

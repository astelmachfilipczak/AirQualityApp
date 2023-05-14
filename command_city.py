from get_stations_data import get_stations_data
from get_sensors_data import get_sensors_data
from get_measurements_data import get_measurements_data
from tkinter import *
import tkinter as tk
import sqlite3

def command_city():
    """
        Funkcja wyświetla listę wszytskich stacji pomiarowych, następnie umożliwia filtrowanie po nazwie
        miejscowości, po czym wyświetla dane pomiarowe.

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
        result = cursor.fetchall()

        # dodanie wyników zapytania do listboxa:
        for row in result:
            listbox.insert(tk.END, row)

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

    def show_city():
        # usunięcie zawartości listboxa:
        listbox.delete(0, END)

        # Pobieranie nazwy miejscowości:
        city_name = str(entry_city.get())

        # wykonanie zapytania SQL:
        cursor.execute('SELECT * FROM stations WHERE city_name = ?', (city_name,))

        # pobranie wyników zapytania:
        result = cursor.fetchall()

        # dodanie wyników zapytania do listboxa:
        for row in result:
            listbox.insert(tk.END, row)

    # Utworzenie okna i wyznaczenie jego rozmiaru:
    root = tk.Tk()
    root.title("AirQualityApp")
    root.geometry('1200x700')

    tk.Label(root, text="---Wyszukaj stację po nazwie miejscowości---").pack()
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
    label_city = Label(frame, text="PODAJ NAZWĘ MIEJSCOWOŚCI W CELU WYŚWIETLENIA DOSTĘPNYCH STACJI:")
    label_staionId = Label(frame, text="PODAJ ID STACJI W CELU WYŚWIETLENIA STANOWISK POMIAROWYCH:")
    label_id = Label(frame, text="PODAJ ID STANOWISKA W CELU WYŚWIETLENIA DANYCH POMIAROWYCH:")

    entry_city = Entry(frame, bd=5)
    entry_staionId = Entry(frame, bd=5)
    entry_id = Entry(frame, bd=5)

    button_city = Button(frame, text="Szukaj", command=show_city)
    button_stationId = Button(frame, text="Szukaj", command=show_sensors_data)
    button_id = Button(frame, text="Szukaj", command=show_measurements_data)

    # rozmieszczenie elementów:
    label_city.grid(row=0, column=0, padx=10)
    label_staionId.grid(row=1, column=0, padx=10)
    label_id.grid(row=2, column=0, padx=10)

    entry_city.grid(row=0, column=1, padx=10)
    entry_staionId.grid(row=1, column=1, padx=10)
    entry_id.grid(row=2, column=1, padx=10)

    button_city.grid(row=0, column=2, padx=10)
    button_stationId.grid(row=1, column=2, padx=10)
    button_id.grid(row=2, column=2, padx=10)

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

if __name__ == '__main__': command_city()
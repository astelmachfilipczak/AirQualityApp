from geopy.distance import great_circle
from get_stations_data import get_stations_data
from get_sensors_data import get_sensors_data
from get_measurements_data import get_measurements_data
from tkinter import *
import tkinter as tk
import sqlite3
from geopy.geocoders import Nominatim


def command_location():

    """
        Funkcja wyświetla listę wszytskich stacji pomiarowych blisko użytkownika i umożliwia przeglądanie w oknie.

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

    def show_stations_by_location():
        # usunięcie zawartości listboxa:
        listbox.delete(0, END)

        # Pobieranie zasięgu i lokalizacji:
        address = str(entry_localization.get())
        radius = float(entry_radius.get())

        # Konwersja adresu na koordynaty
        geolocator = Nominatim(user_agent="11.04")
        location = geolocator.geocode(address)
        user_lat, user_lon = location.latitude, location.longitude

        # Pobranie stacji z bazy danych
        cursor.execute("BEGIN IMMEDIATE")  # dodanie BEGIN IMMEDIATE
        cursor.execute("ALTER TABLE stations ADD COLUMN distance FLOAT")
        cursor.execute("SELECT station_name, gegr_lat, gegr_lon FROM stations")
        stations = cursor.fetchall()

        # Obliczenie odległości między adresem użytkownika a elementami w tabeli 'stations' i dodanie ich do listy
        distances = []
        for row in stations:
            station_name, station_lat, station_lon = row
            distance = great_circle((user_lat, user_lon), (station_lat, station_lon)).km
            if distance <= radius:  # dodaj tylko te stacje, które mieszczą się w zasięgu
                distances.append((row, distance))
                cursor.execute("UPDATE stations SET distance = ? WHERE station_name = ?", (distance, station_name))

        cursor.execute("SELECT * FROM stations WHERE distance <= ?", (radius,))

        # Sortowanie odległości od najbliższej do najdalszej
        stations = cursor.fetchall()
        stations.sort(key=lambda x: x[2])

        cursor.execute("COMMIT")  # zakończenie transakcji
        # Dodanie wyników zapytania do listboxa:
        for row in stations:
            listbox.insert(tk.END, row)

    # Utworzenie okna i wyznaczenie jego rozmiaru:
    root = tk.Tk()
    root.title("AirQualityApp")
    root.geometry('1200x700')

    tk.Label(root, text="---Lista stacji w zadanym promieniu---").pack()
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
    label_localization = Label(frame, text="PODAJ SWOJĄ LOKALIZACJĘ:")
    label_radius = Label(frame, text="PODAJ W JAKIEJ ODLEGŁOŚCI SZUKAĆ STACJI [km]:")
    label_staionId = Label(frame, text="PODAJ ID STACJI W CELU WYŚWIETLENIA STANOWISK POMIAROWYCH:")
    label_id = Label(frame, text="PODAJ ID STANOWISKA W CELU WYŚWIETLENIA DANYCH POMIAROWYCH:")

    entry_localization = Entry(frame, bd=5)
    entry_radius = Entry(frame, bd=5)
    entry_staionId = Entry(frame, bd=5)
    entry_id = Entry(frame, bd=5)

    button_localization = Button(frame, text="Szukaj", command=show_stations_by_location)
    button_stationId = Button(frame, text="Szukaj", command=show_sensors_data)
    button_id = Button(frame, text="Szukaj", command=show_measurements_data)

    # rozmieszczenie elementów:
    label_localization.grid(row=0, column=0, padx=10)
    label_radius.grid(row=1, column=0, padx=10)
    label_staionId.grid(row=2, column=0, padx=10)
    label_id.grid(row=3, column=0, padx=10)

    entry_localization.grid(row=0, column=1, padx=10)
    entry_radius.grid(row=1, column=1, padx=10)
    entry_staionId.grid(row=2, column=1, padx=10)
    entry_id.grid(row=3, column=1, padx=10)

    button_localization.grid(row=1, column=2, padx=10)
    button_stationId.grid(row=2, column=2, padx=10)
    button_id.grid(row=3, column=2, padx=10)

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

if __name__ == '__main__': command_location()
from get_stations_data import get_stations_data
from get_sensors_data import get_sensors_data
from get_measurements_data import get_measurements_data
from tkinter import *
import tkinter as tk
import sqlite3
from PIL import Image, ImageTk


def command_map():
    """
            Funkcja wyświetla położenie na mapie wszytskich stacji pomiarowych i po wyborze wyświetla dane pomiarowe.

            """

    def on_point_click(event):
        station_id = event.widget.find_withtag("current")[0]
        new_window = tk.Toplevel(root)
        new_window.title("Station Info")
        new_window.geometry('300x100')
        entry = tk.Entry(new_window, width=10)
        entry.pack()
        button = tk.Button(new_window, text="Use ID", command=lambda: use_station_id(entry.get()))
        button.pack()

    def use_station_id(station_id):
        print(f"Selected station ID: {station_id}")


    # Utworzenie okna i wyznaczenie jego rozmiaru:
    root = tk.Tk()
    root.title("AirQualityApp")
    root.geometry('900x750')

    # Utworzenie ramki:
    tk.Label(root, text="---Stacje pomiarowe na terenie Polski---").pack()
    tk.Label(root, text="").pack()

    # wczytanie obrazu mapy
    map_image = Image.open("Poland_m.png")
    # map_image = Image.open("mapa_polski.png")
    map_width, map_height = map_image.size
    min_longtitude = 14.15
    max_longtitude = 24.2
    min_latitude = 49
    max_latitude = 54.9

    # utworzenie płótna i wyświetlenie mapy
    canvas = tk.Canvas(root, width=map_width, height=map_height)
    canvas.pack()
    map_image_tk = ImageTk.PhotoImage(map_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=map_image_tk)

    # Wywołanie funkcji w celu zapisu w bazie danych:
    get_stations_data()

    # utworzenie połączenia z bazą danych:
    conn = sqlite3.connect('database.db')

    # utworzenie kursora:
    cursor = conn.cursor()

    # połączenie z bazą danych i pobranie danych stacji pomiarowych
    cursor.execute('SELECT id, gegr_lat, gegr_lon FROM stations')
    stations = cursor.fetchall()

    # dodanie punktów stacji pomiarowych na mapie
    # dodanie callbacka na zdarzenie kliknięcia na punkt z tagiem id
    for id, latitude, longitude in stations:
        x = int((float(longitude) - min_longtitude) * (map_width / (max_longtitude - min_longtitude)))
        y = int((max_latitude - float(latitude)) * (map_height / (max_latitude - min_latitude)))
        station_name = f"Stacja pomiarowa {id}"
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red", tags=(id,))
        canvas.create_text(x, y + 10, text=str(id), tags=(id), font=("Arial", 6))
        canvas.tag_bind(id, "<Button-1>", on_point_click)

    conn.close()
    root.mainloop()

command_map()
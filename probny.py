

from get_stations_data import get_stations_data
from get_sensors_data import get_sensors_data
from get_measurements_data import get_measurements_data

import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
def show_station_name(event):
    id = event.widget.find_closest(event.x, event.y)[0]
    canvas.create_text(event.x, event.y-10, text=id, font=("Arial", 10), tags=(id))


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

print(stations)

# utworzenie listy stacji
station_list = []

# dodanie punktów stacji pomiarowych na mapie
for id, latitude, longitude in stations:
    x = int((float(longitude) - min_longtitude) * (map_width / (max_longtitude - min_longtitude)))
    y = int((max_latitude - float(latitude)) * (map_height / (max_latitude - min_latitude)))

    # utworzenie punktu na mapie i przypisanie tagów
    punkty = canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="red", tags=(id,))
    napisy = canvas.create_text(x, y + 10, text=str(id), tags=(id,), font=("Arial", 6))

    # opóźnienie przypisania funkcji do tagów punktów
    canvas.tag_bind(int(id), '<Enter>', show_station_name)
    canvas.tag_bind(int(id), '<Leave>', lambda event: canvas.delete(id))

    # dodanie stacji do listy
    station_list.append([id, punkty, napisy])

# wydrukowanie listy stacji
print(station_list)

conn.close()
root.mainloop()

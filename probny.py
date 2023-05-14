from get_stations_data import get_stations_data
from get_sensors_data import get_sensors_data
from get_measurements_data import get_measurements_data
from tkinter import *
import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from print_analysis import AnalysisWindow
''''''

def command_map():
    """
            Funkcja wyświetla położenie na mapie wszytskich stacji pomiarowych i po wyborze wyświetla dane pomiarowe.

            """
    def show_measurements_data():
        # usunięcie zawartości listboxa:
        listbox.delete(0, END)

        # Pobieranie danych pomiarowych wybranego stanowiska:
        id = int(entry_id.get())
        get_measurements_data(id)

        # utworzenie połączenia z bazą danych:
        conn = sqlite3.connect('database.db')

        # utworzenie kursora:
        cursor = conn.cursor()

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

        # utworzenie połączenia z bazą danych:
        conn = sqlite3.connect('database.db')

        # utworzenie kursora:
        cursor = conn.cursor()

        # wykonanie zapytania SQL:
        cursor.execute('SELECT * FROM sensors')

        # pobranie wyników zapytania:
        result = cursor.fetchall()

        # dodanie wyników zapytania do listboxa:
        for row in result:
            listbox.insert(tk.END, row)


    def on_point_click(event):
        tag = event.widget.gettags("current")[0]
        new_window = tk.Toplevel()
        new_window.title("AirQualityApp")
        new_window.geometry('900x750')
        tag_label = tk.Label(new_window, text=f"---Stacja o id: {tag}---")
        tag_label.pack()
        # tag_entry = tk.Entry(new_window)
        # tag_entry.insert(0, tag)
        # tag_entry.pack()

        frame = Frame(new_window)
        frame.pack(fill=BOTH, expand=NO)

        # # Utworzenie listboxa:
        global listbox
        listbox = Listbox(new_window)
        listbox.pack(side=TOP, fill=BOTH, expand=YES)

        # Utworzenie suwaka i przypisanie go do listboxa:
        scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        # wprowadzamy elementy interfejsu:
        label_staionId = Label(frame, text="PODAJ ID STACJI W CELU WYŚWIETLENIA STANOWISK POMIAROWYCH")
        label_id = Label(frame, text="PODAJ ID STANOWISKA W CELU WYŚWIETLENIA DANYCH POMIAROWYCH")
        label_analysis = Label(frame, text="DOKONAJ ANALIZY DANYCH")


        global entry_staionId
        entry_staionId = Entry(frame, bd=5)
        entry_staionId.insert(0, tag)
        global entry_id
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



    # Utworzenie okna i wyznaczenie jego rozmiaru:
    root = tk.Tk()
    root.title("AirQualityApp")
    root.geometry('900x750')

    # Utworzenie ramki:
    tk.Label(root, text="---Stacje pomiarowe na terenie Polski---").pack()
    tk.Label(root, text="").pack()

    # wczytanie obrazu mapy
    map_image = Image.open("Poland_map.png")
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



    #  dodanie punktów  i podpisów stacji pomiarowych na mapie:
    for id, latitude, longitude in stations:
        x = int((float(longitude) - min_longtitude) * (map_width / (max_longtitude - min_longtitude)))
        y = int((max_latitude - float(latitude)) * (map_height / (max_latitude - min_latitude)))
        # rysowanie okręgu reprezentującego stację
        circle=canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="black", tags=(id))
        canvas.create_text(x, y + 10, text=str(id), font=("Arial", 6))
        canvas.tag_bind(circle, "<Button-1>", on_point_click)



    conn.close()
    root.mainloop()


command_map()

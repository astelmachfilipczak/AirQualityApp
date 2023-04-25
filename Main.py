"----------------------------------------AirQualityApp----------------------------------------"


# Aplikacja pobiera dane dotyczące badań jakości powietrza w Polsce, publikowane bezpłatnie przez Główny Inspektorat
# Ochrony Środowiska (GIOŚ) i zapisuje je w bazie danych. Zapisane dane prezentowane są w formie wykresu,
# a następnie dokonywana jest analiza danych.


from command_full import command_full
from command_city import command_city
from command_location import command_location
from command_map import command_map


import tkinter as tk



# Utworzenie okna i wyznaczenie jego rozmiaru:
root = tk.Tk()
root.title("AirQualityApp")
root.geometry('575x300')

label1 = tk.Label(root, text="---Witaj w AirQualityApp!---").pack()
label2 = tk.Label(root, text="---Aplikacji służącej do przeglądania danych pomiarowych---").pack()
label3 = tk.Label(root, text="Wybierz jedną z poniższych opcji, aby rozpocząć:").place(x=25, y=100, width=250, height=30)

# Przyciski menu głównego:
tk.Button(root, text="Pełna lista stacji pomiarowych", command=command_full).place(x=25, y=150, width=250, height=30)
tk.Button(root, text="Wyszukaj stacje po nazwie miejscowości", command=command_city).place(x=300, y=150, width=250, height=30)
tk.Button(root, text="Wyszukaj najbliżej położone stacje", command=command_location).place(x=25, y=200, width=250, height=30)
tk.Button(root, text="Wybierz punkt na mapie", command=command_map).place(x=300, y=200, width=250, height=30)


root.mainloop()






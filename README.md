# AirQualityApp

AirQualityApp to aplikacja monitorująca jakość powietrza w Polsce. 
Wyświetla dane publikowane bezpłatnie przez Główny Inspektorat Ochrony Środowiska (GIOŚ) i zapisuje je w bazie danych, a następnie prezentuje dane oraz przeprowadza ich analizę.

## Opis

Do uruchomienia aplikacji służy główny moduł Main. 
Stanowi menu z czterema opcjami nawigacji do wyboru, każda opcja podpięta jest do osobnej funkcji. 
W sytuacji braku łączności aplikacja wyświetla dane "historyczne" - poprzednie wyszukiwanie, niezależnie od wprowadzanych informacji przez użytkownika.

## Struktura aplikacji
```
AirQualityApp/
│
├── venv/
│   └── ... (pliki i katalogi związane ze środowiskiem wirtualnym)
├── command_city.py
├── command_full.py
├── command_location.py
├── command_map.py
├── database.db
├── get_measurements_data.py
├── get_sensors_data.py
├── get_stations_data.py
├── Main.py
├── measurements_analysis.py
├── measurements.json
├── Poland_map.png
├── print_analysis.py
├── README.md
├── sensors.json
├── stations.json
├── test_database.db
├── test_get_measurements_data.py
├── test_get_sensors_data.py
├── test_get_stations_data.py
└── test_get_measurements_analysis.py
```

## Biblioteki

Moduł korzysta z następujących bibliotek Pythona:

- Tkinter - moduł do tworzenia interfejsu użytkownika,
- sqlite3 - moduł do łączenia z bazą danych database.db,
- geopy - moduł do geolokalizacji,
- PIL - moduł do otwierania, edycji, zapisywania i przetwarzania różnych formatów graficznych,
- requests - moduł do wykonywania zapytań sieciowych,
- json - moduł do konwersji danych między formatem JSON a obiektami Pythona,
- pandas - moduł, który został wykorzystany do generowania dataframe,
- matplotlib - moduł, który został wykorzystany w celu generowania wykresów.

Dodatkowo do przeprowadzenia testów uzyto:
- unittest - moduł do przeprowadzania testów,
- os - moduł do wykonywania operacji na plikach.

## Instalacja zależności

Aby zainstalować moduł za pomocą pip install, wykonaj następujące kroki:

1. Otwórz wiersz poleceń lub terminal.
2. Wpisz polecenie pip install nazwa_modułu, gdzie nazwa_modułu to nazwa modułu, który chcesz zainstalować. 
Na przykład, jeśli chcesz zainstalować moduł numpy, wpisz pip install numpy.
3. Naciśnij klawisz Enter, aby uruchomić polecenie.

Upewnij się, że masz zainstalowane narzędzie pip, które jest standardowym menedżerem pakietów dla Pythona. 
Jeśli go nie masz, zapoznaj się z dokumentacją Pythona, aby go zainstalować.

## Instrukcja uruchomienia programu

1. Upewnij się, że masz zainstalowane wyżej wymienione biblioteki. Jeśli nie, zainstaluj je (patrz **Instalacja zależności**).
2. Skopiuj wszystkie pliki projektu do wybranego katalogu.
3. Otwórz główny moduł "Main" w edytorze Python, na przykład w PyCharm.
4. Uruchom moduł "Main".
5. Aplikacja AirQualityApp zostanie uruchomiona, a na ekranie pojawi się interfejs użytkownika.

## Używanie aplikacji

Po uruchomieniu aplikacji AirQualityApp, będziesz mieć do wyboru cztery opcje nawigacji:

**1. Pełna lista stacji pomiarowych:** Ta opcja wyświetli pełną listę dostępnych stacji pomiarowych.
- Po wpisaniu numeru ID stacji pomiarowej kliknij przycisk "Szukaj", a wyświetli się lista dostępnych stanowisk pomiarowych. 
- Następnie wpisz numer ID stanowiska pomiarowego i kliknij dedykowany do ikienka przycisk "Szukaj", co spowoduje wyświetlenie się wykresu danych.
- Po zamknięciu okna wykresu zobaczysz listę zebranych danych pomiarowych.
- W celu dokonania analizy danych kliknij przycisk "Analiza danych" i obserwuj jak pojawia się okienko "Analiza pomiarów".
- Kliknięcie przycisku "Analizuj" spowoduje wygenerowanie wykresu z linią trendu.
- Zamknięcie okna wykresu spowoduje wyświetlenie się przeanalizowanych danych.

**2. Wyszukaj stacje po nazwie miejscowości:** Ta opcja umożliwi wyszukiwanie stacji na podstawie nazwy miejscowości.
- Po wpisaniu nazwy miejscowości kliknij przycisk "Szukaj" w celu wyświetlenia stacji pomiarowych dostępnych w wybranej miejscowości.
- Następnie postępuj zgodnie z instrukcją zamieszczoną w **punkcie 1**.

**3. Wyszukaj najbliżej położone stacje:** Ta opcja pozwoli na wyszukiwanie najbliżej położonych stacji pomiarowych.
- Po wpisaniu nazwy miejscowości oraz zasięgu [km] kliknij przycisk "Szukaj" w celu wyświetlenia najbliższych, zgodnie z zadanym zasięgiem, dostępnych stacji pomiarowych.
- Następnie postępuj zgodnie z instrukcją zamieszczoną w **punkcie 1**.

**4. Wybierz punkt na mapie:** Ta opcja umożliwi wybór punktu na mapie i wyświetlenie stacji pomiarowych w jego pobliżu.
- Na wyświetlonej mapie kliknij w wybrany znacznik stacji pomiarowej.
- Numer ID klikniętej stacji pomiarowej wyświetli się automatycznie w okienku wyboru stacji. 
- Następnie postępuj zgodnie z instrukcją zamieszczoną w **punkcie 1**.

## Licencja

Aplikacja AirQualityApp jest udostępniona na zasadzie FREEWARE. 
Oznacza to, że można korzystać z niej za darmo i używać w dowolnej ilości kopii całkowicie bez ograniczeń!

## Autorzy

Aleksandra Stelmach-Filipczak



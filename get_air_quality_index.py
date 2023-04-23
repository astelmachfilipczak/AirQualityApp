"----------------------------------------MODUŁ: get_air_quality_index----------------------------------------"
import requests
import sqlite3
import json

def get_air_quality_index(stationId):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    # Tworzenie tabeli 'air_quality_index'
    conn.execute('''CREATE TABLE IF NOT EXISTS air_quality_index (
                    id INTEGER PRIMARY KEY REFERENCES stations(id),
                    st_calc_date TEXT,
                    st_index_level_id INTEGER,
                    st_index_level_name TEXT,
                    st_source_data_date TEXT,
                    so2_calc_date TEXT,
                    so2_index_level INT,
                    so2_source_data_date TEXT,
                    st_index_status BOOL,
                    st_index_cr_param TEXT)''')
    try:
    # Pobieranie listy zebranych danych indeksu z wybranej stacji i zapisanie danych do pliku air_quality_index.json:
        air_quality_index = requests.get(('https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/') + str(stationId)).json()

        with open('air_quality_index.json', 'w') as f:
            json.dump(air_quality_index, f)

    except requests.exceptions.RequestException as e:

        # W przypadku błędu wczytywanie danych z plików
        print('BŁĄD POBIERANIA. WCZYTUJĘ DANE HISTORYCZNE...')
        with open('air_quality_index.json', 'r') as f:
            air_quality_index = json.load(f)

    # # Wypełnianie tabeli 'air_quality_index'
    conn.execute('''INSERT INTO air_quality_index (id, st_calc_date, st_index_level_id, st_index_level_name, st_source_data_date, so2_calc_date, so2_index_level, so2_source_data_date, st_index_status, st_index_cr_param)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 (air_quality_index['id'], air_quality_index['stCalcDate'], air_quality_index['stIndexLevel']['id'],
                  air_quality_index['stIndexLevel']['indexLevelName'], air_quality_index['stSourceDataDate'],
                  air_quality_index['so2CalcDate'], air_quality_index['so2IndexLevel']['indexLevelName'],
                  air_quality_index['so2SourceDataDate'], air_quality_index['stIndexStatus'],
                  air_quality_index['stIndexCrParam']))

    # Wykonanie zapytania SELECT do tabeli 'air_quality_index'
    print('LISTA DOSTĘPNYCH STACJI:')
    cursor.execute("SELECT * FROM air_quality_index")

    # Pobranie wszystkich wierszy z wyniku zapytania
    rows = cursor.fetchall()

    # Iteracja po wierszach i wydrukowanie ich na ekranie
    for row in rows:
        print(row)

    conn.commit()
    conn.close()



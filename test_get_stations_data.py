# "----------------------------------------TEST: get_stations_data----------------------------------------"
#
# import unittest
# import sqlite3
# import json
# import os
# import requests_mock
#
# from get_stations_data import get_stations_data
#
# class TestGetStationsData(unittest.TestCase):
#     """
#     Klasa testuje funkcję pobierającą dane ze strony internetowej GIOŚ i zapisującą je do pliku 'stations.json'.
#     """
#
#     # Przygotowuje stan przed wykonaniem testu:
#     def setUp(self):
#         pass
#
#
#     def test_get_stations_data(self):
#         """
#         Funkcja testuje pobieranie danych ze strony GIOŚ, tj. sprawdza czy funkcja pobiera dane ze strony internetowej
#         i zapisuje je do pliku 'stations.json'.
#         """
#         #Przygotowanie odpowiedzi mockowej:
#         with requests_mock.Mocker() as mock:
#             stations = [{'id': 1, 'stationName': 'Station1', 'gegrLat': '12.345', 'gegrLon': '67.890',
#                          'city': {'id': 1, 'name': 'City1',
#                                   'commune': {'communeName': 'Commune1', 'districtName': 'District1',
#                                               'provinceName': 'Province1'}},
#                          'addressStreet': 'Address1'}]
#             mock.register_uri('GET', 'http://api.gios.gov.pl/pjp-api/rest/station/findAll', json=stations)
#
#         # Wywołanie funkcji get_stations_data():
#         get_stations_data()
#
#         # Sprawdzenie czy plik stations.json został utworzony i czy zawiera oczekiwane dane:
#         assert os.path.isfile('stations.json')
#         with open('stations.json', 'r') as f:
#             data = json.load(f)
#         assert data == stations
#
#     def read_stations_json(self, file_path):
#
#
#         with open(file_path, 'r') as f:
#             data = json.load(f)
#         return data
#
#
#
#     def test_stations_data_to_dict(self):
#         """
#         Testowanie odczytu danych z pliku 'stations.json', czyli sprawdzenie, czy funkcja poprawnie odczytuje dane z pliku
#         'stations.json' i przetwarza je na obiekt typu lista słowników. Dodatkowo sprawdzane jest czy lista nie jest pusta
#         oraz czy słowniki zawierają potrzebne przy dalszym wyszukiwaniu klucze 'stationId' i 'id'.
#         """
#         data = self.read_stations_json('stations.json')
#         assert isinstance(data, list)
#         assert len(data) > 0
#         assert all(isinstance(station, dict) for station in data)
#         assert all('id' in station and 'stationName' in station for station in data)
#
#     def create_test_data(self):
#         """
#         Funkcja tworząca testowe dane stacji pomiarowych.
#         """
#         stations = [
#             {
#                 "id": 1,
#                 "stationName": "Station 1",
#                 "gegrLat": "50.1111",
#                 "gegrLon": "19.2222",
#                 "city": {
#                     "id": 1,
#                     "name": "City 1",
#                     "commune": {
#                         "communeName": "Commune 1",
#                         "districtName": "District 1",
#                         "provinceName": "Province 1"
#                     }
#                 },
#                 "addressStreet": "Address 1"
#             },
#             {
#                 "id": 2,
#                 "stationName": "Station 2",
#                 "gegrLat": "51.1111",
#                 "gegrLon": "20.2222",
#                 "city": {
#                     "id": 2,
#                     "name": "City 2",
#                     "commune": {
#                         "communeName": "Commune 2",
#                         "districtName": "District 2",
#                         "provinceName": "Province 2"
#                     }
#                 },
#                 "addressStreet": "Address 2"
#             }
#         ]
#
#         with open('stations.json', 'w') as f:
#             json.dump(stations, f)
#
#     def test_create_stations_table(self):
#         """
#         Testowanie, czy funkcja poprawnie utworzyła tabelę 'stations' i czy tabela zawiera właściwe kolumny.
#         """
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#
#         #Wywołanie testowanej funkcji:
#         get_stations_data()
#         # Sprawdzenie, czy tabela 'stations' została utworzona:
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stations'")
#         result = cursor.fetchone()
#         self.assertIsNotNone(result)
#
#         # Sprawdzenie, czy tabela 'stations' zawiera właściwe kolumny:
#         cursor.execute("PRAGMA table_info(stations)")
#         result = cursor.fetchall()
#         expected_result = [
#                 (0, 'id', 'INTEGER', 1, None, 1),
#                 (1, 'station_name', 'TEXT', 0, None, 0),
#                 (2, 'gegr_lat', 'TEXT', 0, None, 0),
#                 (3, 'gegr_lon', 'TEXT', 0, None, 0),
#                 (4, 'city_id', 'INTEGER', 0, None, 0),
#                 (5, 'city_name', 'TEXT', 0, None, 0),
#                 (6, 'commune_name', 'TEXT', 0, None, 0),
#                 (7, 'district_name', 'TEXT', 0, None, 0),
#                 (8, 'province_name', 'TEXT', 0, None, 0),
#                 (9, 'address_street', 'TEXT', 0, None, 0)
#             ]
#         self.assertEqual(result, expected_result)
#
# # Oznaczenie modułu jako główny, w celu przeprowadzenia testów
# if __name__ == '__main__':
#         unittest.main()

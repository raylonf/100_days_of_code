import requests
from flight_data import FlightData
from data_uteis import TEQUILA_URL, TEQUILA_KIWI_API_KEY


class FlightSearch:

    def get_iata_code(self, city_name):
        header = {'apikey': TEQUILA_KIWI_API_KEY}
        parametros = {'term': city_name}
        response = requests.get(url=f'{TEQUILA_URL}/locations/query', headers=header, params=parametros)
        code = response.json()['locations'][0]['code']

        return code

    def check_flights(self, origin_city_code, destiny_city_code, from_time, to_time):

        header = {'apikey': TEQUILA_KIWI_API_KEY}
        parametros = {
            'fly_from': origin_city_code,
            'fly_to': destiny_city_code,
            'sort': 'price',
            "flight_type": "round",
            "one_for_city": 1,
            'max_stopovers': 0,
            'date_from': '',
            'date_to':'',
            'nights_in_dts_from': 7,
            'nights_in_dts_to': 28,
            'curr': 'BRL',
        }
        response = requests.get(url=f'{TEQUILA_URL}/search', headers=header, params=parametros)

        try:
            data = response.json()['data'][0]
        except:
            print(f'No flights found for {destiny_city_code}.')
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][1]['local_departure'].split('T')[0]

        )

        print(f'{flight_data.destination_city}: £{flight_data.price}')

        return flight_data


from data_uteis import GOOGLE_SHEETY_URL, TEQUILA_URL, TEQUILA_KIWI_API_KEY
import requests


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=GOOGLE_SHEETY_URL)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        header = {'apikey': TEQUILA_KIWI_API_KEY}
        for d in self.destination_data:
            parametros = {
                'term': d['city']
            }
            response = requests.get(url=f'{TEQUILA_URL}/locations/query', headers=header, params=parametros)
            code = response.json()['locations'][0]['code']
            d['iataCode'] = code

        id = 2
        for data in self.destination_data:
            body = {
                'price': data
            }
            response = requests.put(url=f'{GOOGLE_SHEETY_URL}/{id}', json=body)
            id += 1

            return response.text

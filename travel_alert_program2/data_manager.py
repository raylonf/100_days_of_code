from data_uteis import LINK_SHEETS_URL, FILE_SERVICE_ACCOUNT, TEQUILA_KIWI_API_KEY, TEQUILA_URL
import requests
import gspread


class DataManager:

    def __init__(self):
        gc = gspread.service_account(filename=FILE_SERVICE_ACCOUNT)
        workspreed = gc.open_by_url(url=LINK_SHEETS_URL)
        self.list_flights = workspreed.worksheet('prices')
        self.destination_data = {}

    def get_destination_data(self):
        self.destination_data = self.list_flights.get()[1:]
        return self.destination_data

    def update_destination_codes(self):
        header = {'apikey': TEQUILA_KIWI_API_KEY}
        for d in self.destination_data:

            if d[1] == '':
                parametros = {
                    'term': d[0]
                }
                response = requests.get(url=f'{TEQUILA_URL}/locations/query', headers=header, params=parametros)
                code = response.json()['locations'][0]['code']
                d[1] = code
                row = 2
                for data in self.destination_data:
                    self.list_flights.update_cell(value=data[1], col=2, row=row)
                    row += 1
            else:
                continue
        # print(self.destination_data)



if __name__ == '__main__':
    new = DataManager()
    new.get_destination_data()
    new.update_destination_codes()
import requests
from pprint import pprint
import datetime as dt
from twilio.rest import Client

GOOGLE_SHEETY_URL = 'https://api.sheety.co/17b8df78a73b29a8c80fc39a81d0614a/flightDeals/prices'
TEQUILA_URL = 'https://tequila-api.kiwi.com'
TEQUILA_KIWI_API = 'xn4YWKmux9scmCOC5bnYsG9BJtDPsxA9'
account_sid = 'AC4125d3e090b4d7e89629b203fbf2ac8c'
auth_token_twilio = 'e828f30170e44e529095e0d2d3859687'


# UPDATE_GOOGLE_SHEETY_URL = f'{GOOGLE_SHEETY_URL}/{id}'

def sendSMS(to_phone, msg=str):
    client = Client(account_sid, auth_token_twilio)
    message = client.messages.create(
        body=msg,
        from_='+12344054495',
        to=to_phone
    )

    return message.sid


header = {
    'apikey': TEQUILA_KIWI_API
}

response = requests.get(url=GOOGLE_SHEETY_URL)
data = response.json()
sheety_data = data['prices']
# print(sheety_data)

# for d in sheety_data:
#     parametros = {
#         'term': d['city']
#     }
#     response = requests.get(url=f'{TEQUILA_URL}/locations/query', headers=header, params=parametros)
#     code = response.json()['locations'][0]['code']
#     d['iataCode'] = code

# pprint(data['prices'])
# pprint(sheety_data)

# id = 2
# for data in sheety_data:
#     body = {
#         'price': data
#     }
#
#     print(body)
#     response = requests.put(url=f'{GOOGLE_SHEETY_URL}/{id}', json=body)
#     id += 1
#     print(response.text)

# parametros = {
#     'term': 'Paris'
# }

# r = requests.get(url=f'{TEQUILA_URL}/locations/query', headers=header, params=parametros)
# dta = r.json()['locations'][0]['code']
# print(dta)

yesterday = dt.datetime.today() - dt.timedelta(days=1)
day_return = yesterday + dt.timedelta(days=6 * 30)

for d in sheety_data:

    parametros = {
        'fly_from': 'LON',
        'fly_to': d['iataCode'],
        'sort': 'price',
        'max_stopovers': '0',
        'date_from': yesterday.strftime('%d/%m/%Y'),
        'date_to': day_return.strftime('%d/%m/%Y'),
        'nights_in_dts_from': '7',
        'nights_in_dts_to': '28',
        'curr': 'GBP',
        'partner_market': 'us'
    }
    response = requests.get(url=f'{TEQUILA_URL}/search', headers=header, params=parametros)
    preços_caros = response.json()['data'][-1]['price']
    preços_baratos = response.json()['data'][0]['price']
    city_to = f"{response.json()['data'][0]['cityTo']}-{response.json()['data'][0]['countryTo']['code']}"
    arrivaltime = response.json()['data'][0]['aTimeUTC']
    # print(dt.datetime.fromtimestamp(arrivaltime))
    # print(f'{d["city"]}: ${preços_baratos}')
    # print(response.json()['data'][0])
    if preços_baratos < d['lowestPrice']:
        msg = f"Low price alert, Only £{preços_baratos} to fly from London-{response.json()['data'][0]['countryFrom']['code']} to {city_to}, from {dt.datetime.fromtimestamp(arrivaltime)}"
        sendSMS(to_phone='+5534991676814', msg=msg)

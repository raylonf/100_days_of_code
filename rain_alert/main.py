import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

messagem_tempo = ''
api_key_weather = 'e2abd315fc6afd364ec67edcfff9934a'
account_sid = 'AC4125d3e090b4d7e89629b203fbf2ac8c'
auth_token_twilio = 'e828f30170e44e529095e0d2d3859687'



def sendSMS(to_phone):
    global messagem_tempo, account_sid, auth_token_twilio
    # proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid, auth_token_twilio)
    message = client.messages.create(
        body=f'Bring a Umbrela, it is going to rain today , {messagem_tempo} ⛈',
        from_='+12344054495',
        to=to_phone
    )

    return message.sid



long = -48.2772
lati = -18.9186

weather_api = 'https://api.openweathermap.org/data/2.5/onecall?'  # lat={lat}&lon={lon}&exclude={part}&appid={API key}'
city = 'uberlandia,BR'

parametros = {
    'lat': lati,
    'lon': long,
    'exclude': 'daily,minutely,current,alerts',
    'units': 'metric',
    'lang': 'pt_br',
    'appid': api_key_weather
}

response = requests.get(weather_api, params=parametros)
response.raise_for_status()
data = response.json()
weather_condiction = data['hourly']
will_rain = False

for c in range(0, 12):

    horas = 9
    for i in weather_condiction[c]['weather']:
        if i['id'] < 700:
            messagem_tempo = i['description']
            will_rain = True

if will_rain:
    print(sendSMS('+5534991676814'))
    sendSMS('+5534991488758')

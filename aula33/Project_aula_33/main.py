import requests
import datetime as dt
import smtplib
from time import sleep

MY_LAT = -18.9025771
MY_LNG = -48.3221404
MY_EMAIL = 'raylonsilva42@gmail.com'
PASSWORD = 'v^1@brNVPs2'

parametros = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

frase = 'Subject:Olhe para o céu\n\nA estação internacional espacial (ISS) está proximo de você, procure que vc irá encontrar.'


def iss_on_position():
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    lat_iss = int(float(data_iss['iss_position']['latitude']))
    long_iss = int(float(data_iss['iss_position']['longitude']))
    if int(MY_LAT) + 5 >= lat_iss >= int(MY_LAT) - 5 and int(MY_LNG) + 5 >= long_iss >= int(MY_LNG) - 5:
        return True


def on_time():
    response_time = requests.get('https://api.sunrise-sunset.org/json', params=parametros)
    response_time.raise_for_status()
    data_sunrise = int(response_time.json()['results']['sunrise'].split('T')[1].split(':')[0]) - 3
    data_sunset = int(response_time.json()['results']['sunset'].split('T')[1].split(':')[0]) - 3
    data_now = dt.datetime.now()
    hour_now = int(data_now.hour)
    if hour_now < data_sunrise or hour_now > data_sunset:
        return True


while True:
    sleep(60)
    if iss_on_position() and on_time():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='raylon.f@hotmail.com', msg=frase.encode('utf-8'))


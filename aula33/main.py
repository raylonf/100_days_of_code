MY_LAT = -18.9025771
MY_LNG = -48.3221404


# import urllib.request
# import json
#
# req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
# response = urllib.request.urlopen(req)
#
# obj = json.loads(response.read())
#
# print(obj['timestamp'])
# print(obj['iss_position']['latitude'] +' '+ obj['iss_position']['latitude'])

import requests
import json
import datetime as dt

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
# data = response.json()['iss_position']
# longitude = data['longitude']
# latitude = data['latitude']
# print(data)
# print(longitude)
# print(latitude)

parametros = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parametros)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f'Sunrise: {sunrise},\n'
      f'Sunset: {sunset}')

time_now = dt.datetime.now()
print(time_now)

# {'results': {'sunrise': '6:06:34 AM', 'sunset': '6:15:26 PM', 'solar_noon': '12:11:00 PM', 'day_length': '12:08:52', 'civil_twilight_begin': '5:46:54 AM', 'civil_twilight_end': '6:35:06 PM', 'nautical_twilight_begin': '5:22:48 AM', 'nautical_twilight_end': '6:59:12 PM', 'astronomical_twilight_begin': '4:58:42 AM', 'astronomical_twilight_end': '7:23:18 PM'}, 'status': 'OK'}

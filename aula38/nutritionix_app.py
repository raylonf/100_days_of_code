import requests
import datetime as dt


SHEETY_TOKEN_API = '2gU/fdY9N!vxqm'
SHEETY_URL = 'https://api.sheety.co/17b8df78a73b29a8c80fc39a81d0614a/myWorkouts/workouts'
NUTRITIONIX_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
APP_ID = '7e68df99'
APP_KEY = '22750dadfb4a664f31c4e518cc6c5769'

today = dt.datetime.today().strftime('%d/%m/%Y')
horario = dt.datetime.now().time().strftime('%H:%M:%S')

exercicios = input('Tell me which exercicies you did? ')

header = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

parametros = {
    'query': exercicios
}

response = requests.post(url=NUTRITIONIX_URL, json=parametros, headers=header)
data_response = response.json()['exercises']
for data in data_response:
    exerc = data['name']
    duration = data['duration_min']
    calories = data['nf_calories']
    body = {
        'workout':{
            'date': today,
            'time': horario,
            'exercise': exerc,
            'duration': duration,
            'calories': calories
        }
    }
    header_sheety = {'Authorization': f'Bearer {SHEETY_TOKEN_API}'}
    response = requests.post(url=SHEETY_URL, headers=header_sheety, json=body)
    print(response.json())

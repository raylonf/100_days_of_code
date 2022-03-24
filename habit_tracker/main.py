import requests
import datetime as dt

USERNAME = 'raylon'
TOKEN = 'dflasjdpoelqwjrwl54f4sa2'
GRAPH_ID = 'graph1'
date = dt.datetime.today()
# print(date.strftime('%Y%m%d'))



pixela_url = 'https://pixe.la/v1/users'
# pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_url}/{USERNAME}/graphs'
pixel_endpoint_post = f'{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_edit_put = f'{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime("%Y%m%d")}'

user_params = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)


graph_config = {
    'id':'graph1',
    'name':'Swiming Graph',
    'unit': 'meters',
    'type':'float',
    'color':'sora',
    'timezone':'UTC -3'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

pixel_post = {
    'date': '20220308',
    'quantity': input('How many meters you swimming today?')

}

pixel_edit_post = {
    'quantity': '1400'
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=pixel_endpoint_post, headers=headers, json=pixel_post)
print(response.text)

# response = requests.get(url='https://pixe.la/v1/users/raylon/graphs/graph1.html')

# response = requests.put(url=pixel_edit_put, headers=headers, json=pixel_edit_post)
# print(response.text)
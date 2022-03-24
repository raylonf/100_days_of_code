import requests
from data_uteis import USUARIOS_URL


def check_user_exist(email):
    usuarios = Users.get_all_user()
    exist = True
    for data in usuarios['users']:
        print(data)
        if email == data['email']:
            print('User have been registered.')
            exist = False
    if exist is False:
        return False



class Users:

    def __init__(self):
        self.first_name = '',
        self.last_name = '',
        self.email = ''

    def cadastro_user(self, first_name, last_name, email):
        body = {
            'user':{
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        if check_user_exist(email):
            response = requests.post(url=USUARIOS_URL, json=body)
            self.first_name = first_name,
            self.last_name = last_name,
            self.email = email
            return response.text

    def get_all_user():
        response = requests.get(url=USUARIOS_URL)

        return response.json()

    def edit_user(self, userID, new_first_name, new_last_name, new_email):
        body = {
            'user': {
                'firstName': new_first_name,
                'lastName': new_last_name,
                'email': new_email
            }
        }
        response = requests.put(url=f'{USUARIOS_URL}/{userID}', json=body)
        self.first_name = new_first_name,
        self.last_name = new_last_name,
        self.email = new_email

        return response.text

    def delete_user(userID):
        response = requests.delete(url=f'{USUARIOS_URL}/{userID}')

        return response.text


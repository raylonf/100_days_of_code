import requests
from pprint import pprint
import datetime as dt
from data_uteis import GOOGLE_SHEETY_URL, TEQUILA_URL, TEQUILA_KIWI_API_KEY
import users



print(users.Users.get_all_user())

print("Welcome to Raylon's Flight Club.")
print("We find the best flight deals and email you")
Fname = input("What's your first name?\n")
Lname = input("What's your last name?\n")
email_to_save = input("What's your email?\n")
while True:
    remail = input('Confirm your email\n')
    if email_to_save == remail:
        cad = users.Users()
        cad.cadastro_user(first_name=Fname, last_name=Lname, email=email_to_save)

        print("You're in the club!")
        break


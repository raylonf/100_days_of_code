import requests

get_cadastro_url = 'https://api.sheety.co/17b8df78a73b29a8c80fc39a81d0614a/flightDeals/users'
post_new_email_url = 'https://api.sheety.co/17b8df78a73b29a8c80fc39a81d0614a/flightDeals/users'


print("Welcome to Raylon's Flight Club.")
print("We find the best flight deals and email you")
Fname = input("What's your first name?\n")
Lname = input("What's your last name?\n")
email_to_save = input("What's your email?\n")
while True:
    remail = input('Confirm your email\n')
    if email_to_save == remail:
        print("You're in the club!")
        break
#
body = {
    'user':{
        'firstName': Fname,
        'lastName': Lname,
        'email': email_to_save
    }
}

response = requests.post(url=post_new_email_url, json=body)
print(response.text)


# response = requests.get(url=get_cadastro_url)
# print(response.text)
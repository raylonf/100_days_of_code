##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
import random

my_email = 'raylonsilva42@gmail.com'
password = 'v^1@brNVPs2'

letters = []
file = pd.read_csv('birthdays.csv')
file_dict = file.to_dict(orient='records')
# print(file_dict)

todaynow = dt.datetime.now()
day = todaynow.day
month = todaynow.month

for x in range(1, 4):
    with open(f'letter_templates/letter_{x}.txt') as file:
        letter = file.read()
        letters.append(letter)

name_email = []

for n in file_dict:
    if day == n['day'] and month == n['month']:
        name_email.append((n['xname'], n['email']))

if name_email != 0:
    for n in range(len(name_email)):
        name = name_email[n][0]
        email = name_email[n][1]
        new_letter = random.choice(letters)
        new_letter = new_letter.replace('[NAME]', name)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email,
                                msg=f'Subject:Happy Birthday\n\n{new_letter}')

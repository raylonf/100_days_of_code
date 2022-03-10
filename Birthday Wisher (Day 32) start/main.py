# import random
# import smtplib


# my_email = 'raylonsilva42@gmail.com'
# password = 'v^1@brNVPs2'


# connection = smtplib.SMTP('smtp.gmail.com', 587)
# connection.starttls()  ##Deixa a conexão segura##
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs='raylon.f@hotmail.com', msg='Subject:Ola\n\nThis is body of my email test')
# connection.close()
#
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()  ##Deixa a conexão segura##
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='raylon.f@hotmail.com',
#                         msg='Subject:Ola\n\nThis is body of my email test'
#                         )
#
# import datetime as dt
#
# now = (dt.datetime.now())
# year = now.year
# month = now.month
# day_of_week = now.weekday() #0- segunda 1- terça 2-quarta , etc#
# print(now)
# print(year)
# print(month)
# print(day_of_week)
#
# date_of_birthdate = dt.datetime(year=1990, month=12, day=29, hour=3)
# print(date_of_birthdate)
import random
import datetime as dt
import smtplib


today = dt.datetime.now()
weektoday = today.weekday()
frase = []
if weektoday == 0:
    with open('quotes.txt', 'r') as file:
        frases = file.read().split('\n')
        frase = random.choice(frases)

    my_email = 'raylonsilva42@gmail.com'
    password = 'v^1@brNVPs2'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='raylon.f@hotmail.com', msg=f'Subject:Motivational Message\n\n{frase}')


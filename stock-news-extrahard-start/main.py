import requests
import html
from twilio.rest import Client
import datetime as dt



alphavantage_key = '4V89E9SUPODRT4QZ'
newsapi_key = '24606cdb5f4b484a98e3c2f226932b56'
account_sid = 'AC4125d3e090b4d7e89629b203fbf2ac8c'
auth_token_twilio = 'e828f30170e44e529095e0d2d3859687'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
day_today = dt.datetime.today().date()



def sendSMS(to, body):
    client = Client(account_sid, auth_token_twilio)
    message = client.messages.create(
        body=body,
        from_='+12344054495',
        to=to
    )

    print(message.status)


parametros_bolsa_valores = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'datatype': 'json',
    'apikey': alphavantage_key
}

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=parametros_bolsa_valores)
data = r.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]


preço_dia = float(data_list[0]['4. close'])
preço_anterio = float(data_list[1]['4. close'])
variação = (preço_dia - preço_anterio) / preço_anterio * 100

if variação >= 2 or variação <= -5:
    print('Get News')
    url_news = 'https://newsapi.org/v2/everything'
    parametros_news = {
        'q': COMPANY_NAME,
        'from': day_today,
        'sortBy': 'popularity',
        'encode': 'utf-8',
        'apiKey': newsapi_key
    }
    response = requests.get(url_news, params=parametros_news)
    data_news = html.unescape(response.json())
    last_news = data_news['articles'][:3]

    if variação >= 5:
        for data in last_news:
            message = f'TSLS: 🔺{int(variação)}%\n' \
                      f'Headline: {data["title"]}\n' \
                      f'Brief: {data["description"]}.'
            sendSMS('+5534991676814', message)

    else:
        for data in last_news:
            message = f'TSLS: 🔻{int(variação*-1)}%\n' \
                          f'Headline: {data["title"]}\n' \
                          f'Brief: {data["description"]}.'
            sendSMS('+5534991676814', message)

# print(data)
print(variação)
# print(preço_dia)
# print(preço_anterio)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
coronavirus market crash.
"""


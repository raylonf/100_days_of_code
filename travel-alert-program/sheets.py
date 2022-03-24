import gspread

KEY = 'AIzaSyD5m9VniWcuzLcdPQliKRnP2nmAkEw-b3U'
# CONTA-SERVIÇO-ID = 'travel-alert@firm-foundation-345013.iam.gserviceaccount.com'
FILE_SERVICE_ACCOUNT = 'C:\\Users\\raylo\Downloads\\firm-foundation-345013-be46e114e62f.json'
gc = gspread.service_account(filename=FILE_SERVICE_ACCOUNT)
header = {'key': KEY}
list = gc.open_by_url(url='https://docs.google.com/spreadsheets/d/1j2bdGc_0aJd4uYy6y5t6kYhMLfQpCa4nvJ92BF7oFyU/edit#gid=0')
list_prices = list.worksheet('prices')
list_user = list.worksheet('users')


print(list_prices.get())
print(list_user.get())


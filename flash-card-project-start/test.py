import pandas as pd
import random

data = pd.read_csv('data/french_words.csv')
data_dict = data.to_dict(orient='records')
datadic = data.to_dict()
del data_dict[41]
words = pd.DataFrame(data_dict)
wor = words.to_csv()


print(data_dict)
print(wor)

data_saved = pd.read_csv('data/words_to_learn.csv')
data_french = data_saved['French']
data_english = data_saved['English']
words_to_learn = data_saved.to_dict(orient='records')
# data_french = data['French']
# rand = random.randint(0, len(data_french))
# print(data_french[rand])

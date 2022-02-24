#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dic = {rows.letter: rows.code for (index, rows) in nato_data_frame.iterrows()}
# while True:
#     word = input('Enter a word: ')
#     try:
#         letters = [nato_dic[letter.upper()] for letter in word]
#         print(letters)
#         break
#     except:
#         print('Sorry, only letters in the alphabet please')

def generate_phonetc():
    word = input('Enter a word: ')
    try:
        letters = [nato_dic[letter.upper()] for letter in word]
    except:
        print('Sorry, only letters in the alphabet please')
        generate_phonetc()
    else:
        print(letters)

generate_phonetc()
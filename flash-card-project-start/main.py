from tkinter import *
import pandas as pd
import random
# import os
BACKGROUND_COLOR = "#B1DDC6"


data_french = []
data_english = []
rand = None
recent_card = None
words_to_learn = {}


def load():
    global data_english, data_french, words_to_learn
    # if os.path.exists('data/word_to_learn.csv'):
    try:
        data_saved = pd.read_csv('data/word_to_learn.csv')
        data_french = data_saved['French']
        data_english = data_saved['English']
        words_to_learn = data_saved.to_dict(orient='records')
    # else:
    except:
        data = pd.read_csv('data/french_words.csv')
        data_french = data['French']
        data_english = data['English']
        words_to_learn = data.to_dict(orient='records')
        print('Error')



def next_card():
    global rand, flip_timer, recent_card, data_english, data_french, data
    window.after_cancel(flip_timer)
    rand = random.randint(0, len(data_french))
    canvas.itemconfig(canvas_image, image=image_front)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_text, text=data_french[rand], fill='black')
    flip_timer = window.after(3000, func=flip_card)
    recent_card = rand


def next_card_right():
    global rand, recent_card, words_to_learn
    del words_to_learn[recent_card-1]
    # with open('data/word_to_learn.csv', 'w') as file:
    #     data_words = pd.DataFrame(words_to_learn)
    #     file.write(data_words.to_csv())
    data_words = pd.DataFrame(words_to_learn)
    data_words.to_csv('data/word_to_learn.csv', index=False)
    next_card()


def flip_card():
    global rand
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_text, text=data_english[rand], fill='white')


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file='images/card_front.png')
image_back = PhotoImage(file='images/card_back.png')
image_button_right = PhotoImage(file='images/right.png')
image_button_wrong = PhotoImage(file='images/wrong.png')
canvas_image = canvas.create_image(400, 263, image=image_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
card_text = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

right_button = Button(image=image_button_right, highlightthickness=0, command=next_card_right)
right_button.grid(row=1, column=1)

wrong_button = Button(image=image_button_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

load()
next_card()

window.mainloop()

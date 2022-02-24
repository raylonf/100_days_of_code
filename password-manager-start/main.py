from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = [choice(string.ascii_letters) for _ in range(randint(4, 10))]
    symbols = [choice(string.punctuation) for _ in range(2, 4)]
    numbers = [str(randint(0, 9)) for _ in range(2, 4)]
    passw = letters + symbols + numbers
    shuffle(passw)
    password = ''.join(passw)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    if len(website_input.get()) != 0 and len(username_input.get()) != 0 and len(password_input.get()) != 0:
        new_data = {
            website: {
                'email': email,
                'password': password,
            }
        }
        if messagebox.askokcancel(message=f'Do you want save:\n{new_data}', title='Save'):
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    data.update(new_data)

            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)

            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showinfo(title='Oops', message='Please make sure you have not left any fields empty.')

# ---------------------------- SEARCH ------------------------------- #


def search():
    if len(website_input.get()) != 0:
        try:
            with open('data.json', 'r') as file:
                data_search = json.load(file)
                if data_search[website_input.get()]:
                    email = data_search[website_input.get()]['email']
                    password = data_search[website_input.get()]['password']
                    messagebox.showinfo(title=website_input.get(), message=f'Email: {email}\nPassword: {password}')
                    print(data_search[website_input.get()]['email'])
        except KeyError:
            messagebox.showinfo(title='Error', message='No Data File Found')
        except FileNotFoundError:
            messagebox.showinfo(title='Error', message='No details for the website exists')
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username: ')
username_label.grid(row=2, column=0)

password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

generate_passw_button = Button(text='Generate Password', command=generator)
generate_passw_button.grid(row=3, column=2)

add_button = Button(text='Add', command=save)
add_button.config(width=44)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', command=search)
search_button.config(width= 13)
search_button.grid(row=1, column=2)

website_input = Entry()
website_input.config(width=35)
website_input.grid(row=1, column=1)
website_input.focus()

username_input = Entry()
username_input.config(width=53)
username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry()
password_input.config(width=35)
password_input.grid(row=3, column=1)

window.mainloop()

3435363738393

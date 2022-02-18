from tkinter import *

window = Tk()
window.title('Raylon Program')
window.minsize(width=500, height=300)
#para que as bordas nao encontre com as caixas(label, botões, etc)
window.config(padx=20, pady=20)

# Label
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.place(x= 0, y= 200)
my_label.grid(column=0, row=0)

my_label['text'] = 'New Text'
# or #
my_label.config(text='Next Text')
my_label.config(padx= 50, pady=10)
# Button
def button_clicked():

    my_label['text'] = input.get()


button1 = Button(text='Click me', command=button_clicked)
button1.grid(column=2, row=2)

button2 = Button(text='Click me')
button2.grid(column=3, row=1)

#Entry
input = Entry(width=20)
# input.pack()
input.grid(column=4, row=3)
print(input.get())



window.mainloop()

from tkinter import *

def convert_mile_to_km():
    x = int(entrykm.get()) * 1.609
    label_convert.config(text=f'{x:.2f}')


window = Tk()
window.title('Mile to Km Converter')
# window.minsize(height=200, width=300)
window.config(padx=20, pady=20)

entrykm = Entry(width=10)
# entrykm.insert()
# entrykm.getint(self=0)
entrykm.grid(column=3, row=1)

label_miles = Label(text='Miles')
label_miles.grid(column=5, row=1)

label_inf = Label(text='is equal to')
label_inf.grid(column=1, row=3)

label_convert = Label(text='0')
label_convert.grid(column=3, row=3)

label_km = Label(text='Km')
label_km.grid(column=5, row=3)

button = Button(text='Calculate', command=convert_mile_to_km)
button.grid(column=3, row=5)








window.mainloop()
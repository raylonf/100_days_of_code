import turtle
from prettytable import PrettyTable

"""
tymmy = turtle.Turtle()
tymmy.shape('turtle')
tymmy.color('cyan')
my_window = turtle.Screen()
my_window.exitonclick()"""

table = PrettyTable()
table.field_names = ["Pokemon name", "Type"]
table.add_rows([
    ['Pikachu', 'Electric'],
    ['Squirtle', 'Water'],
    ['Charmander', 'Fire']
])
print(table)
table.align = 'l'
print(table)
#List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
new_numbers = [n for n in numbers]
print(new_numbers)

name = 'Angela'
letters_list = [letter for letter in name]
print(letters_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [n * n for n in numbers]


#Write your code 👆 above:

print(squared_numbers)

#List comprehension with condicional
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freedie']
short_names = [n for n in names if len(n) < 5]
long_names = [n.upper() for n in names if len(n) > 5]

print(short_names)
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0 ]

#Write your code 👆 above:

print(result)



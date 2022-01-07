import random
import string

passw = []
letters = ''
symbols = ''
numbers = ''

print('---------WELCOME PASSWORD GENERATOR ----------')
print('')
print('')
x = int(input('How many letters you want in your password?\n'))
y = int(input('How many symbols woud you like?\n'))
z = int(input('How many numbers woud you like?\n'))

for c in range (0, x):
    letters = random.choice(string.ascii_letters)
    passw.append(letters)

for c in range(0, y):
    symbols = random.choice(string.punctuation)
    n = random.randint(0, len(passw))
    passw.insert(n, symbols)

for c in range(0, z):
    numbers = random.randint(0, 9)
    n = random.randint(0, len(passw))
    passw.insert(n, str(numbers))
    
passwd = ''.join(passw)

print(f'Your password is: {passwd}\n')

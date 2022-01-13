import random
import string


class PasswordGenerator:
    def __init__(self):
        pass   
    
    def generator(self, qntLetters, qntSymbols ,qntNumbers):
        passw = []
        letters = ''
        symbols = ''
        numbers = ''
        
        for c in range (0, qntLetters):
            letters = random.choice(string.ascii_letters)
            passw.append(letters)

        for c in range(0, qntSymbols):
            symbols = random.choice(string.punctuation)
            n = random.randint(0, len(passw))
            passw.insert(n, symbols)

        for c in range(0, qntNumbers):
            numbers = random.randint(0, 9)
            n = random.randint(0, len(passw))
            passw.insert(n, str(numbers))
            
        passwd = ''.join(passw)

        return passwd
    
    
print('\n---------WELCOME PASSWORD GENERATOR ----------')
print('')
print('')
x = int(input('How many letters you want in your password?\n'))
y = int(input('How many symbols woud you like?\n'))
z = int(input('How many numbers woud you like?\n'))


s = PasswordGenerator()
ax = s.generator(qntLetters= x, qntSymbols= y, qntNumbers= z)

print(f'Your password is: {ax}\n')




        

from typing import Counter


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1.lower
name2.lower
y = 0

x = (name1+name2).lower()
y = x.count('t') + x.count('r') + x.count('u') + x.count('e')
a = x.count('t' or 'u')

z = x.count('l') + x.count('o') + x.count('v') + x.count('e')
print(a)

total = y *10 + z
if total <= 10 or total >= 90:
    print (f'Your score is {total}, you go together like coke and mentos.') 
elif 40 <= total <= 50 :
    print(f'Your score is {total}, you are alright together.')
else:
    print(f'Your score is {total}.')
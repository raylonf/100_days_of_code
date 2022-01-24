import random

number = random.randint(1,100)
print('''\n  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  ''')

print('\n-#-#-#-#-Welcome to the Number Guessing Game!-#-#-#-#-\n')
print("I'm thinking of a number between 1 and 100.\n")
diff = input("Choose a difficult. Type 'easy' or 'hard': ").lower()

while True:
    if diff == 'easy':
        n = 10
        break
    elif diff == 'hard':
        n = 5
        break
    else:
        print('Option invalid!')
        diff = input("Choose a difficult. Type 'easy' or 'hard': ").lower()

print(f'You have {n} attempts remaining to guess the number.\n')
guess = int(input('Make a guess: '))

while True:
    if n == 0:
        print("You've run out of guess, you lose.")
        break
    
    if guess == number:
        print(f'You got it. The answer was {number}.')
        break
    
    if guess != number:
        if guess < number:
            print('Too low.')
        else:
            print('Too high.')
        n -= 1
        print(f'You have {n} attempts remaining to guess the number.\n')
        
    guess = int(input('Make a guess: '))

        
        
import os

print(''' 
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\ ''')

resp = 'yes'
mydic = {}
winner_name = ''    
maior = 0
print('')
while resp == 'yes':
    name = input("What's your name? ")
    bid = int(input("What's your bid?$ "))
    mydic[name] = bid
    resp = input("Are there any others bidders? Type 'yes' or 'no'.\n").strip()
    
    
    os.system('cls') or None    
    
    if resp == 'no':        
        for c in (mydic):
            if maior == 0:
                maior == mydic[c]
                winner_name = c
            if mydic[c] > maior:
                maior = mydic[c]
                winner_name = c
            
        print(f"The winner is {winner_name} with a bid of ${maior}")

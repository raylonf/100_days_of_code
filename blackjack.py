############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def start_hand(list):
    for c in range(2):
        c = random.choice(cards)
        list.append(c)
    if list[0] == 11 and list[1] == 11:
        list.pop()  
        list.append(1)

def get_card(list):
    list.append(random.choice(cards2))
        
def current_score(list):
    n = 0
    for c in list:
         n += c         
    return n


logo = '''.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           '''
      
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_hand = []
dealer_hand = []
blackjack = False
blackjack_dealer = False

start = input("\nDo you want to play a game of BlackJack? Type 'y' or 'n': ")

while start == 'y':
    your_hand.clear()
    dealer_hand.clear()
    start_hand(your_hand)
    start_hand(dealer_hand)
    
    if current_score(your_hand) == 21:
        blackjack = True
        
    if current_score(dealer_hand) == 21:
        blackjack_dealer = True
    
    print(f"Your cards: {your_hand}, current_score: {current_score(your_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}")
    
    while True:
        resp = input("Type 'y' to get another card, type 'n' to pass: ")[0].lower()
        if resp == 'y':
            get_card(your_hand)            
            if current_score(your_hand) >= 21:
                break
            else:
                print(f"Your cards: {your_hand}, current_score: {current_score(your_hand)}")
        if resp == 'n':
            break
        
    print(f"Your final hand: {your_hand}, current score: {current_score(your_hand)}")
    
    while current_score(dealer_hand) < 16:
        get_card(dealer_hand)
        
    print(f"Computer final hand: {dealer_hand}, current score: {current_score(dealer_hand)} ")
    
    if current_score(your_hand) == current_score(dealer_hand):
        print('Draw ')

    elif blackjack == True and blackjack_dealer == False:
        print('Win with BlackJack!!')
        blackjack = False
        
    elif blackjack_dealer == True and blackjack == False:
        print('You lose with BlackJack!!')
        blackjack_dealer = False
        
    elif current_score(your_hand) <= 21 and current_score(your_hand) > current_score(dealer_hand) :
        print('You win')
    
    elif current_score(your_hand) > 21 :
        print('You went over. You lose ')
    
    elif current_score(dealer_hand) > 21 and current_score(your_hand) <= 21:
        print('You win ')
        
    else:
        print('You lose ')
    
    start = input("\nDo you want to play a game of BlackJack? Type 'y' or 'n': ")
    







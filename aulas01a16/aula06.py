print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total = 0

preços = {'S': 15, 'M': 20, 'L': 25}

total += preços[size]
if add_pepperoni == 'Y' and size == 'S':
    total += 2
elif add_pepperoni == 'Y' :
    total += 3
    
if extra_cheese == 'Y':
    total += 1

print(total)
    
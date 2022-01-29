MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_coffee(coffee):
    
    if resources['water'] < MENU[coffee]['ingredients']['water']: 
        print("Sorry there is not enough water. ")
        return False
      
    if resources["coffee"] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there is not enough coffee. ") 
        return False  
     
    if coffee == 'latte' or coffee == 'cappuccino':
        if resources["milk"] < MENU[coffee]['ingredients']['milk']:
            print("Sorry there is not enough milk. ")
            return False
        else:
            return True    
    else:
        return True

def check_payment(coffee):
    
    quarter = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    pennies = int(input('How many pennies: '))
    payment = (quarter * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
    if payment < MENU[coffee]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False    
    
    else:
        if 'fundos' not in resources:       
            resources['fundos'] = MENU[coffee]['cost'] 
        else:
            resources['fundos'] += MENU[coffee]['cost']                    
        change = payment - MENU[coffee]['cost']
        
        if change == 0:
            print("It's ok")
        else:
            print(f'Here is ${change:.2f} in change')
                        
        return True

def make_coffee(coffee):          
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources["coffee"] -= MENU[coffee]['ingredients']['coffee']
    try:
        resources["milk"] -= MENU[coffee]['ingredients']['milk']
    except:
        pass
    
    print(f'Here is your {coffee} ☕️. Enjoy!')

def stock():
    print(f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]} g')
    try:
        print(f'Money: ${resources["fundos"]}')
    except:
        pass

while True:           
    drink = input('What wold you like? (espresso/latte/cappuccino) ')
    if drink == 'report':
        stock()
    
    elif drink == 'price':
        print(f'Espresso: ${MENU["espresso"]["cost"]:.2f} \nLatte: ${MENU["latte"]["cost"]:.2f}\nCappuccino: ${MENU["cappuccino"]["cost"]:.2f}')
            
    elif drink == 'espresso' or drink == 'latte' or drink == 'cappuccino':              
        if check_coffee(drink) is True:           
            if check_payment(drink) is True:            
                make_coffee(drink)
    elif drink == 'stock up':
        stock()
        w = int(input('How many ml of water you want replenish? '))
        m = int(input('How many ml of milk you want replenish? '))
        c = int(input('How many g of coffee you want replenish? '))
        resources['water'] += w
        resources['milk'] += m
        resources['coffee'] += c
        stock()
        
        
    else:
        print('Invalid option!')

import os


def cal(x, y, operation):
    if operation == '+':
        return x + y
    if operation == '-':
        return x - y
    if operation == '*':
        return x * y
    if operation == '/':
        return x / y


logo = ''' _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
print(logo)

while True:
    number = float(input("What's your first number? "))
    print('+\n-\n/\n*')
    operation = input('Pick an operation: ')[0]
    while operation not in '+-*/':
        print('Operation invalid!')
        operation = input('Pick an operation: ')[0]
    second_number = float(input("What's next number: "))
    result = cal(number, second_number, operation)
    print(f'{number} {operation} {second_number} = {result}')
    resp = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    while resp not in 'yn':
        resp = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    while resp == 'y':
        number = result
        operation = input('Pick an operation: ')
        second_number = float(input("What's next number: "))
        result = cal(number, second_number, operation)
        print(f'{number} {operation} {second_number} = {result}')
        resp = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    if resp == 'n':
        os.system('cls') or None
        print(logo)
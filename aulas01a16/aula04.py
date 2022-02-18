#Exercicío de ano de Bissexto

year = int(input("Which year do you want to check? "))

if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print('Leap year.')
#elif year % 100 == 0 :
 #   print ('Not leap year.')
else:
    print ('Not leap year.')
def prime_checker(number):
    s = 0
    for c in range (1, number +1):
        if number % c == 0:
            s += 1
       
    if s == 2:
        print('primo')
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
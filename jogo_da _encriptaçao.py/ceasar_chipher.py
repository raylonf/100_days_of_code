
from encrypt_decrypt_ceapher import *
import os


logo2 = ''' ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
again = ''
print('')
print(logo2)
print('')

while True:
    resp = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").strip().lower()
    while True:
        if resp == 'encode':
            break

        elif resp == 'decode':
            break  
            
        else:
            print('Error, type your choice.')
            resp = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").strip().lower()
            
    os.system('cls') or None
        
    message = input('\nType your message:\n')
    shift = int(input('\nType the shift number:\n'))
    
    os.system('cls') or None
    
    if resp == 'encode':
        x = encrypt(message, shift)
        print(f"Here's the encoded result: {x}")
    else:
        x = decrypt(message, shift)
        print(f"Here's the decoded result: {x}")

         
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    if again == 'no':
        print('Goodbye')
        break
    

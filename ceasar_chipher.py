from lista_palavras import logo2
from encrypt_decrypt_ceapher import *
import os

logo = logo2
again = ''
print('')
print(logo)
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
        break
    

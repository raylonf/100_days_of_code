import string


letter_lower = list(string.ascii_lowercase)
letter_uper = list(string.ascii_uppercase)
digits = list(string.digits)


def encrypt(message, shift):
    message_encrypt = []
    message = list(message)
    for c in message:
        if c == ' ':           
            message_encrypt.append(c)              
        if c.isnumeric:
            for d in range(0, len(digits)):
                if c == digits[d]:
                    y = d + shift
                    while y > 9:
                        y -= 9
                    message_encrypt.append(digits[y])    
        
        if c.isupper:
            for i in range (0, len(letter_uper)):
                if c == letter_uper[i]:
                    w = i + shift
                    while w > 25:
                        w -=26
                    message_encrypt.append(letter_uper[w])                  
    
        if c.islower:
            for d in range (0, len(letter_lower)):
                if c == letter_lower[d]:
                    x = d + shift
                    while x > 25:
                        x -=26
                    message_encrypt.append(letter_lower[x])       
    m = ''.join(message_encrypt)
    return m

def decrypt(message, shift):
    message_encrypt = []
    message = list(message)
    for c in message:
        if c == ' ':           
            message_encrypt.append(c)              
        if c.isnumeric:
            for d in range(0, len(digits)):
                if c == digits[d]:
                    y = d - shift
                    while y < 0:
                        y += 9
                    message_encrypt.append(digits[y])    
        
        if c.isupper:
            for i in range (0, len(letter_uper)):
                if c == letter_uper[i]:
                    w = i - shift
                    while w < 0:
                        w +=26
                    message_encrypt.append(letter_uper[w])                  
    
        if c.islower:
            for d in range (0, len(letter_lower)):
                if c == letter_lower[d]:
                    x = d - shift
                    while x < 0:
                        x +=26
                    message_encrypt.append(letter_lower[x])       
    m = ''.join(message_encrypt)
    return m


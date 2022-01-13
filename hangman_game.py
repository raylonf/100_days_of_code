import os
import random

d = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
     );
def linha(n, cor = 0):
    print(d[cor], end='')
    print('~' * (len(n) + 4))
    print(f'  {n}')
    print('~' * (len(n) + 4))
    print(d[0], end='')


nomes = ['bike', 'bicicleta', 'moto', 'carro', 'escola', 'garagem', 'apartamento']
nome_random = nomes[random.randint(0, len(nomes)-1)]
forca = [''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||    
| |          ||__
| |         (    )
| |         ( __ )
| |        
| |       
| |      
| |     
| |          
| |          
| |          
| |          
| |         
""""""""""|         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''', ''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         
| |        
| |       
| |      
| |     
| |          
| |          
| |          
| |          
| |         
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''' , ''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |         Y . . Y
| |          |   | 
| |          | . |  
| |          |   |   
| |          
| |          
| |          
| |         
| |         
""""""""""|         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''', ''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y . . Y
| |       // |   | 
| |      //  | . |  
| |     ')   |   |   
| |          
| |          
| |          
| |          
| |        
""""""""""|         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''', ''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y . . Y \\
| |       // |   | \ \\
| |      //  | . |  \ \\
| |     ')   |   |   (`
| |          
| |         
| |          
| |         
| |         
""""""""""|         |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''', ''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\`_.'
| |         .-`--'.
| |        /Y . . Y \\
| |       // |   | \ \\
| |      //  | . |  \ \\
| |     ')   |   |   (`
| |          ||'
| |          || 
| |          || 
| |          || 
| |         / | 
""""""""""|_`-'     |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''',''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y \\
| |       // |   | \ \\
| |      //  | . |  \ \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
''']

print('''                                                                              
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
   ''')

n = input("Let's play? ")

os.system('cls') or None

    
x = '_' * len(nome_random)
x = list(x)
z = len(nome_random)
m = 0
errorletters = []
x1 = ' '.join(x)
print(x1)

print('')

while m != z :
    y = input('Guess a letter: ').lower()[0]
    os.system('cls') or None
    if y in nome_random:
        print("Ok, it's in the word \n")
        
        if y in x:
            (print('But you alredy say this letter.\n'))
        else:
            for c in range(0, len(nome_random)):
                if y == nome_random[c]:
                    x.insert(c, y)
                    del x[c + 1]
                    
    if '_' not in x:
        linha('      ******    Congratulations    ******      ', 5)
        break
           
    elif y not in nome_random:
        print(f"You guessed {y}, that's not in the word. You lose your live.")
        errorletters.append(y)
        print(errorletters)
        if len(errorletters) == 6:
            print(forca[len(errorletters)])
            linha(  '        Game Over     ', 1)
            break
        
    x2 = ' '.join(x)
    print('')
    print(x2)       
    print(forca[len(errorletters)])

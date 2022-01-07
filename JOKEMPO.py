import random
from time import sleep

jogos = 0
vit_j1 = 0
vit_pc = 0
resp = ''

def jogar_pc(x):
    if x == 0:
        return 'Pedra'
    if x == 1:
        return 'Papel'
    if x == 2 :
        return 'Tesoura' 
    
        
print('Jokem Po')

print('Vamos jogar?')

while resp != 'N':
    resp = input('Gostaria de jogar?(S/N) ')[0].upper()
    if resp == 'S':
        print('Vai ser uma melhor de 5, ok? ')
        print('')
        while jogos != 5:
            if resp == 'S':
                J1 = input('Qual você escolhe? (Pedra/ Papel/ Tesoura) ').capitalize()
                print('')
                Jpc = jogar_pc(random.randint(0, 2))
                sleep(0.5)
                print('JO')
                sleep(0.3)
                print('KEM')
                sleep(0.3)
                print('PO')
                sleep(0.5)
                print('')
                print(Jpc)
                print('')
                
                if J1 == 'Pedra' and Jpc == 'Tesoura' or J1 == 'Papel' and Jpc == 'Pedra' or J1 == 'Tesoura' and Jpc == 'Papel':
                    vit_j1 += 1
                    jogos += 1
                    print('OK você ganhou :( \nMas da proxima eu te pego!!')
                elif J1 == Jpc:
                    print('AAAHHH empate, vamos de novo, da proxima eu consigo ganhar de você!!')
                else:
                    vit_pc += 1
                    jogos += 1
                    print('Eu te disse que eu era o melhor, se segura, que vou acabar com você! Brinks')
                print('')   
                print(f'Placar é de {vit_j1} vitorias para Jogador e de {vit_pc} vitorias para o pc! ')
                print('')
        if vit_j1 > vit_pc:
            print('Derrota completa :( Aceitaria uma revache uma outra hora? ')
        else:
            print('Vitoria completa!! Agora vou descansar enquanto estou por cima da carne seca! HAHAHAHAHA')
    if resp == 'N':
        print('Arregão, já sabia que você tinha medo de mim! ')
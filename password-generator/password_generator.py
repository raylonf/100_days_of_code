import PySimpleGUI as sg
import random
import string
import json
import os

class PasswordGenerator:
    
    def __init__(self): 
        self.password = ''            
    
    def generator(self, qntLetters, qntSymbols ,qntNumbers):
        passw = []        
                
        for c in range (0, qntLetters):
            letters = random.choice(string.ascii_letters)
            passw.append(letters)

        for c in range(0, qntSymbols):
            symbols = random.choice(string.punctuation)
            n = random.randint(0, len(passw))
            passw.insert(n, symbols)

        for c in range(0, qntNumbers):
            numbers = random.randint(0, 9)
            n = random.randint(0, len(passw))
            passw.insert(n, str(numbers))
            
        self.password = ''.join(passw)
        
        return self.password
    
        #self.login[site] = email, self.password()
               
    def load(self):
        if not os.path.exists('generator_pass.txt'):
            return
        with open('generator_pass.txt', 'r') as f:
            self.login = json.load(f)   
            
           
    def save(self, email, site):
        senha = self.password
        x = {}        
        x[site] = email, senha
        #print('Saving ....')
        with open('generator_pass.txt', 'a') as f:
            json.dump(x,  f)            
        #print('Saved!') 
    
    def window_gerador():
        sg.theme('Reddit')
        layout = [
            [[sg.Text('Email or User')], [sg.Input(key='email')]],
            [[sg.Text('Site')], [sg.Input(key='site')]],
            [sg.Text('How many letters you want in your password?'), sg.Spin(values = [i for i in range(1, 1000)], key= 'letters')],
            [sg.Text('How many symbols would you like?'), sg.Spin(values = [i for i in range(1, 1000)], key= 'symbols')],
            [sg.Text('How many numbers would you like?'), sg.Spin(values = [i for i in range(1, 1000)], key= 'numbers')],
            [sg.In('', key= 'password', size=(50,1))],
            [[sg.Button('Generate'), sg.Button('Save'), sg.Button('Exit')]]
        ]
        return sg.Window('Passaword Generate', layout= layout)
    
    janela = window_gerador()
    
    while True:
        events, value = janela.read()
        
        if events == sg.WINDOW_CLOSED or events == 'Exit':
            break
            
        if events == 'Generate':  
            janela['password'].update(generator(self = janela ,qntLetters= int(value['letters']), qntSymbols=int(value['symbols']), qntNumbers= int(value['numbers'])))          
            
        if events == 'Save' and value['site'] != '':   
            try:                             
                save(self= janela, email= value['email'], site= value['site'])
                sg.popup('Saved')
            except:
                continue
        
          
'''print("\n---------WELCOME PASSWORD GENERATOR ----------")
print('')
print('')
x = int(input('How many letters you want in your password?\n'))
y = int(input('How many symbols would you like?\n'))
z = int(input('How many numbers would you like?\n'))


s = PasswordGenerator()
print(s.generator(qntLetters= x, qntSymbols= y, qntNumbers= z))
s.save('raylon.f', 'ecommerce.com')
'''
#print(f'Your password is: {ax}\n')




        

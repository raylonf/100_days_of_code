from asyncio import events
from socket import timeout
from PySimpleGUI import PySimpleGUI as sg
from encrypt_decrypt_ceapher import *


#Layout
sg.theme('Reddit')
layout = [[sg.Text('Type your message:'), sg.Input(key='message', size=(51,2))],
          [sg.Text('Type the shift number:'), sg.Input(key= 'shift', size=(10,2))],
          [sg.Button('Encode'), sg.Button('Decode')],
          [sg.Text(size=(40,1), key= 'resp')],
          [sg.Output(size=(70,3), key='-OUTPUT-')],
          [sg.Button('Exit')]  
]


#janela
janela = sg.Window(' Caesar Chipher ', layout)


#interações

while True:
    events, values = janela.read()
    if events == sg.WINDOW_CLOSED or events == 'Exit':
        break
    
            
    if events == 'Encode' or events == 'Decode':
        if events == 'Encode':
            #values['resp'] = "Here's the encoded result:"
            values['-OUTPUT-'] = encrypt(message= values['message'], shift= int(values['shift']))
            janela['resp'].update(f"Here's the encoded result: ", text_color = 'Blue')
            print(values['-OUTPUT-'])
            #print(values['-OUTPUT-'] )
            
        elif events == 'Decode':
            #values['resp'] = "Here's the decoded result:"
            values['-OUTPUT-'] = decrypt(message= values['message'], shift= int(values['shift']))
            janela['resp'].update(f"Here's the decoded result: ", text_color = 'red')
            #print(values['resp'])
            print(values['-OUTPUT-'] )
            
      
       
              


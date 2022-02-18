#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pydoc import plain


palavras = []
frases = []
with open(r'aula24\Mail Merge Project Start\Input\Names\invited_names.txt', 'r') as file:
    palavras = file.read().split()


with open('aula24\Mail Merge Project Start\Input\Letters\starting_letter.txt', 'r') as f:
    frase = f.read()

for word in palavras:
    x = frase.replace('[name],', word)
    frases.append(x)

    with open(f'aula24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{word}', 'w') as f:
        f.write(x)
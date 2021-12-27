#Descubra quanto tempo falta em dias, semanas e meses, para completar os 90 anos, baseados com a sua idade atual

age = input("What is your current age?")

rest = 90 - int(age)
x = rest * 365
y = rest * 52
z = rest * 12

print(f'You have {x} days, {y} weeks, and {z} months left.')
#IMC com a sua respectiva classificação 
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

imc = weight/ (height **2)
imc = round(imc)


if imc <= 18.5:
    print(f'Your BMC is {imc}, you are underweight.')
elif imc <= 25:
    print(f'Your BMI is {imc}, you have a normal weight.')
elif imc <= 30:
    print(f'Your BMI is {imc}, you are slightly overweight.')
elif imc <= 35:
    print(f'Your BMI is {imc}, you are obese.')
else:
    print(f'Your BMI is {imc}, you are clinically obese.')

# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos 
#seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não 
#estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
# O símbolo ( representa "maior que". Por exemplo:
#[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
#(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000


num = float(input())

if num >= 0 and num <= 25:
    print ("Intervalo [0,25]", end="\n")
elif num > 25 and num <= 50:
    print ("Intervalo (25,50]", end="\n")
elif num > 50 and num <= 75:
    print ("Intervalo (50,75]", end="\n")
elif num > 75 and num <= 100:
    print ("Intervalo (75,100]", end="\n")
else:
    print ("Fora de intervalo", end="\n")
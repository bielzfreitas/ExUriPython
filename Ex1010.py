# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de 
#cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
#Após, calcule e mostre o valor a ser pago.

entrada = input()
entrada2 = input()
numerosStr = entrada.split(" ")
numerosStr2 = entrada2.split(" ")
numeros = [float(num) for num in numerosStr]
numeros2 = [float(num) for num in numerosStr2]

cod, qtd, val = numeros
cod1, qtd1, val1 = numeros2

valf = (qtd * val) + (qtd1 * val1)

print ("VALOR A PAGAR: R$ {:.2f}".format(valf))
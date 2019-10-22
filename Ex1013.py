# Faça um programa que leia três valores e apresente o maior dos três valores lidos 
#seguido da mensagem “eh o maior”. Utilize a fórmula:
#Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). 
#Um segundo passo, portanto é necessário para chegar no resultado esperado. 

entrada = input()
strnums = entrada.split(" ")
nums = [int(num) for num in strnums]
a, b, c = nums

ab = (a + b + abs(a-b)) / 2
maiorabc = (ab + c + abs(ab-c)) / 2

print (int(maiorabc), "eh o maior")
# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. 
#Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. 
#Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor 
#tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

n = int(input())

for i in range(1 , n + 1 ):
    x = input().split()
    a,b,c = x
    print('{:.1f}'.format((float(a) * 2 + float(b) * 3 + float(c) * 5) / 10))
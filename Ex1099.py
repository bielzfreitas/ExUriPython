# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste 
#consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.
#A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
#Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.
#Imprima a soma de todos valores ímpares entre X e Y.


n = int(input())
d = 0

for c in range(1 , n + 1):
    x = input().split()
    a, b, = x
    s=0
    a = int(a)
    b = int(b)

    if a > b:
        for d in range(int(b)+1, int(a)):
            if d % 2 != 0:
                s = s + d
    if a < b:
        for d in range(int(a)+1, int(b)):
            if d % 2 != 0:
                s = s + d
    if a == b:
        s = 0
    print(s)

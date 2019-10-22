#Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
#Não há nenhuma entrada neste problema.
#Imprima a sequencia conforme exemplo abaixo
#I=1 J=7
#I=1 J=6
#I=1 J=5
#I=3 J=7
#I=3 J=6
#I=3 J=5
#...
#I=9 J=7
#I=9 J=6
#I=9 J=5


i = 1
j = 7

while i <= 9:
    while j >= 5:
        print('I={} J={}'.format(i,j))
        j = j - 1
    i = i + 2
    j = 7
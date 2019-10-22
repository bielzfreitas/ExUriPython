#Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
#Não há nenhuma entrada neste problema.
#Imprima a sequencia conforme exemplo abaixo.
#I=0 J=1
#I=0 J=2
#I=0 J=3
#I=0.2 J=1.2
#I=0.2 J=2.2
#I=0.2 J=3.2
#.....
#I=2 J=?
#I=2 J=?
#I=2 J=?


i = 0
j = 1
acrescimo = (0.2)
n = 0
while i <= 2:
    for c in range(1,4):
        if i > 2.19:
            print('I={:.0f} J={:.0f}'.format(2,j))
        if i == 1.0 or i == 0.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i,j))
        elif i < 2:
            print('I={:.1f} J={:.1f}'.format(i,j))
        j = j + 1
    i = i + acrescimo
    j = 1 + i
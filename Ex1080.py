# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.]
#O arquivo de entrada contém 100 números inteiros, positivos e distintos.
#Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

n = int(input())
x=0

for i in range(1,100):
    a = int(input())
    if a > x:
        maior = a
        posicao = i + 1
        x = a

print(maior)
print(posicao) 
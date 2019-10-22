# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados 
#foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range (1,6):
    v = int (input())
    if v % 2 == 0:
        pares += 1
    else:
        impares += 1

    if v > 0:
        positivos += 1
    elif v < 0:
        negativos += 1

print (str(pares) + ' valor(es) par(es) ')
print (str(impares) + ' valor(es) impar(es) ')
print (str(positivos) + ' valor(es) positivo(s) ')
print (str(negativos) + ' valor(es) negativo(s) ')
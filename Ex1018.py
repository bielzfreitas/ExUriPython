# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o 
#valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
#A seguir mostre o valor lido e a relação de notas necessárias.

ent = int(input())
print (ent)

n100 = int(ent / 100)
n50 = int((ent - n100 * 100) / 50)
n20 = int((ent - n100 * 100 - n50 * 50) / 20)
n10 = int((ent - n100 * 100 - n50 * 50 - n20 * 20) / 10)
n5 = int((ent - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10) / 5)
n2 = int((ent - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5) / 2)
n1 = int(ent - n100 * 100 - n50 * 50 - n20 * 20 - n10 * 10 - n5 * 5 - n2 * 2)

print (int(n100), "nota(s) de R$ 100,00")
print (int(n50), "nota(s) de R$ 50,00")
print (int(n20), "nota(s) de R$ 20,00")
print (int(n10), "nota(s) de R$ 10,00")
print (int(n5), "nota(s) de R$ 5,00")
print (int(n2), "nota(s) de R$ 2,00")
print (int(n1), "nota(s) de R$ 1,00")
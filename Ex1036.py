# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
#caso haja uma divisão por 0 ou raiz de numero negativo.

ent = input().split(" ")
ents = [float(num) for num in ent]
a, b, c = ents

delta = (b ** 2) - 4 * a * c
if delta > 0:
    raiz = sqrt(delta)
else:
    raiz = 0

if (((b * -1) + raiz > 0) or ((b * -1) + raiz < 0)) and (((b * -1) - raiz > 0) or ((b * -1) - raiz < 0)) and raiz > 0:
    r1 = ((b * -1) + raiz) / (2 * a)
    r2 = ((b * -1) - raiz) / (2 * a)
    print ("R1 = {:.5f}".format(r1))
    print ("R2 = {:.5f}".format(r2))
else:
    print ("Impossivel calcular")
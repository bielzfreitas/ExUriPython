# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e 
#p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
#Distancia = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

ent1 = input()
ent2 = input()

strn1 = ent1.split(" ")
strn2 = ent2.split(" ")

num1 = [float(num) for num in strn1]
num2 = [float(num) for num in strn2]

x1, y1 = num1
x2, y2 = num2

res = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print ("{:.4f}".format(res))
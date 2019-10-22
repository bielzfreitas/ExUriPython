# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e 
#o total de combustível gasto (em litros).

dist = int(input())
gast = float(input())

resp = dist / gast

print ("{:.3f}".format(resp), "km/l")
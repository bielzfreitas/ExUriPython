# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
#e informe-o expresso no formato horas:minutos:segundos.

n = int(input())

h = int(n) / 3600
m = (int(n) - (int(h) * 3600)) / 60
s = int(n) - (int(h) * 3600) - (int(m) * 60)

show = str(int(h)) + ":" + str(int(m)) + ":" + str(int(s))

print (show)
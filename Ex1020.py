# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
#Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
#Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
#Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

n = int(input())

ano = int(n) / 365
mes = (int(n) - (int(ano) * 365)) / 30
dias = int(n) - (int(ano) * 365) - (int(mes) * 30)

print (int(ano), "ano(s)")
print (int(mes), "mes(es)")
print (int(dias), "dia(s)")
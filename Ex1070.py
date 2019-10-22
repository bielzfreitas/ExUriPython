# 3. Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, 
#um valor por linha, inclusive o X ser for o caso.

x = int (input())
for i in range (x if x % 2 == 1 else x + 1, x + 12, 2):
    print (i)
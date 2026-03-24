print("Digite quatro valores inteiros:")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b or a == c or a == d or b == c or b == d or c == d:
 print("Os valores precisam ser diferentes.")
else:
 maior = a
 menor = a

 #maior
 if b > maior: maior = b
 if c > maior: maior = c
 if d > maior: maior = d

 #menor
 if b < menor: menor = b
 if c < menor: menor = c
 if d < menor: menor = d

 #segundo menor
 if (a != menor and (a <= b or b == menor) and (a <= c or c == menor) and (a <= d or d == menor)): segundo_menor = a
 elif (b != menor and (b <= a or a == menor) and (b <= c or c == menor) and (b <= d or d == menor)): segundo_menor = b
 elif (c != menor and (c <= a or a == menor) and (c <= b or b == menor) and (c <= d or d == menor)): segundo_menor = c
 else: segundo_menor = d

 #segundo maior
 if (a != maior and (a >= b or b == maior) and (a >= c or c == maior) and (a >= d or d == maior)): segundo_maior = a
 elif (b != maior and (b >= a or a == maior) and (b >= c or c == maior) and (b >= d or d == maior)): segundo_maior = b
 elif (c != maior and (c >= a or a == maior) and (c >= b or b == maior) and (c >= d or d == maior)):segundo_maior = c
 else: segundo_maior = d

 print("Maior valor =", maior)
 print("Menor valor =", menor)
 print("A soma do segundo maior com o segundo menor =", segundo_maior + segundo_menor)
#Ler quatro valores e mostrar em ordem crescente (sem usar o sort da linguagem)

print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b: a,b = b,a
if a > c: a,c = c,a
if a > d: a,d = d,a
if b > c: b,c = c,b
if b > d: b,d = d,b
if c > d: c,d = d,c

print(a,b,c,d)
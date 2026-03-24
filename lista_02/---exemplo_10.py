'''Mostrar a sequência de números abaixo.
Resultado: 
1
2 2
3 2
4 2 4
5 2 4
6 2 4 6
...
10 2 4 6 8 10

Obs: Primeira coluna: números de 1 a 10, demais colunas: números pares menores/iguais ao valor da 1a coluna.'''

for n in range (1, 11):
 print(n, end= "")
 for i in range(2, n + 1, 2):
  print(" ", i, sep="", end="")

 print()
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

n = 1

for n in range (1, 11):
    if n % 2 == 0: 
        print(n)
    else: 
        print(n)
    n += 1
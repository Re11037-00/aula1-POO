'''1. Ler dois valores inteiros e imprimir o maior deles, ou a mensagem "Números iguais", se forem iguais.
Digite dois valores inteiros
1
2
Maior = 2'''

print("Digite dois valores inteiros")
a = int(input())
b = int(input())

if a > b:
    print(f'Maior = {a}')
elif b > a:
    print(f'Maior = {b}')
else:
    print("Números iguais")
'''4. Ler uma sequência de números inteiros separados por vírgula e calcula a soma destes valores.
Digite uma sequência de números separados por vírgula:
1,2,3,4,5
Soma = 15'''

s = input("Digite uma sequência de números separados por vírgula: ")
numeros = s.split(",")
soma = 0

for n in numeros:
    soma += int(n)

print(f'Soma = {soma}')
'''3. Ler uma string, calcular e mostrar a soma dos caracteres que são algarismos.
Digite uma frase:
Brasil 2014
7'''

frase = input('Digite uma frase: ')
soma = 0

for x in frase:
    if x.isdigit():
        soma += int(x)

print(soma)
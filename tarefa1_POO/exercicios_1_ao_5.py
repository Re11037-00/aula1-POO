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


'''2. Ler uma string com dois valores inteiros positivos entre um operador ( +, –, * ou / ) e calcular o resultado da
operação matemática utilizando estes valores e o operador.
Digite dois valores inteiros separados por um operador +, -, * ou /
20+100
O resultado da operação é 120'''

print('Digite dois valores inteiros separados por um operador +, -, * ou /')
operacao = input()

if '+' in operacao: 
    valor = operacao.split('+')
    resultado = int(valor[0]) + int(valor[1])
elif '-' in operacao:
    valor = operacao.split('-')
    resultado = int(valor[0]) - int(valor[1])
elif '*' in operacao:
    valor = operacao.split('*')
    resultado = int(valor[0]) * int(valor[1])
elif '/' in operacao:
    valor = operacao.split('/')
    resultado = int(valor[0]) / int(valor[1])

print(f'O resultado da operação é {resultado}')


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


'''5. Ler os dados de um país: nome, população e área em km2

e calcular sua densidade demográfica. O programa
deve utilizar uma classe País que defina atributos para os dados do país e um método para cálculo da sua
densidade.
Digite o nome do país: Brasil
Digite sua população: 213400000
Digite a área em km2: 8510000
A densidade demográfica do Brasil é de 25,08 hab/km2''' 

class pais:
    def __init__(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0
    def calc_dens(self):
        return self.populacao / self.area
    
x = pais()
x.nome = (input("Digite o nome do país: "))

x.populacao = int(input("Digite sua população: "))

x.area = int(input("Digite a área em km2:"))

a = x.calc_dens()
print(f"A densidade demográfica do {x.nome} é de {a:.2f} hab/km2")
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


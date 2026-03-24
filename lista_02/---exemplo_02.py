#Ler o número do mês (1 – janeiro; 2 – fevereiro; ...; 12 – dezembro) e identificar o nome do mês e em que trimestre o mês está incluído.

print('Informe o número do mês')
mes = int(input())
trimestre = 0

match mes:
    case 1: mes = 'Janeiro', trimestre = 1
    case 2: mes = 'Fevereiro', trimestre = 1
    case 3: mes = 'Março',  trimestre = 1
    case 4: mes = 'Abril', trimestre = 2
    case 5: mes = 'Maio', trimestre = 2
    case 6: mes = 'Junho', trimestre = 2
    case 7: mes = 'Julho', trimestre = 3
    case 8: mes = 'Agosto', trimestre = 3
    case 9: mes = 'Setembro', trimestre = 3
    case 10: mes = 'Outubro', trimestre = 4
    case 11: mes = 'Novembro', trimestre = 4
    case 12: mes = 'Dezembro', trimestre = 4

print(f'O mês de {mes} é do {trimestre} trimestre do ano')

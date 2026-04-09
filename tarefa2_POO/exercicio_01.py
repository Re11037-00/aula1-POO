'''1. Calcular o valor de uma conta de água usando a classe Água. A classe define os atributos mês, ano e consumo para armazenar os dados relativos a uma conta: mês/ano da conta e total consumido em m3. (1m3 = 1000 litros)
A classe deve ter um método para calcular e retornar o valor da conta de água do mês que é calculado da seguinte
forma:

• Até 10 m3, que é denominado consumo mínimo, é cobrado um valor fixo de R$ 38,00

• De 11 a 20 m3, é cobrada uma tarifa extra de R$ 5,00 para cada m3 além do consumo mínimo

• A partir de 21 m3 são cobrados os valores anteriores acrescidos de uma tarifa extra de R$ 6,00 para cada metro cúbico consumido acima de 20m3 

Usando a classe, escreva um programa para ler os dados de uma conta de água do usuário e apresentar o valor a
ser pago.'''


class Agua:
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0
    def calc_conta(self):
        valor = 0
        if self.consumo <= 10:
            valor = 38
        elif self.consumo >= 11 or self.consumo <= 20:
            acima_10 = self.consumo - 10
            valor = 38 + (acima_10 * 5)
        elif self.consumo >= 21:
            acima_10 = self.consumo - 10
            acima_20 = self.consumo - 20
            valor = 38 + (acima_10 * 5) + (acima_20 * 6)
        return valor

x = Agua()
x.mes = int(input("Informe o mês: "))
x.ano = int(input("Informe o ano: "))
x.consumo = float(input("Informe o consumo de água (em m3) durante esse período: "))
a = x.calc_conta()
print(f"A conta de {x.mes}/{x.ano} será de R${a}")
        


    
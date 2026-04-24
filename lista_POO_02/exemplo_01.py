# Entidades
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2

class Circulo:
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, v):
         if v >= 0: self.__raio = v
         else: raise ValueError()
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14 * (self.__raio)**2
    def calc_circumferencia(self):
        return 2 * 3.14 * (self.__raio)
    
class Viagem():
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return (self.__distancia / self.__tempo)
    
class Conta():
    def __init__(self):
        self.__nome = ""
        self.__numero = 0
        self.__saldo = 0.0
    def set_nome(self, n):
        self.__nome = n
    def set_numero(self, v):
        if v >= 0: self.__numero = v
        else: raise ValueError()
    def set_saldo(self, s):
        self.__saldo = s
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def deposito(self, valor):
        self.__saldo += valor
    def saque(self, valor):
        self.__saldo -= valor


class Ingresso():
    def __init__(self):
        self.__dia = ""
        self.__hora = ""
    def set_dia(self, d):
        if d >= 1 and d <= 7: self.__dia = d
        else: raise ValueError()
    def set_hora(self, h):
        if h >= 0 and h <= 24: self.__hora = h
        else: raise ValueError()
    def get_dia(self):
        return self.__dia
    def get_hora(self):
        return self.__hora
    def valor(self): 
        valor_base = 0
        if self.__dia == 4: return 8
        if self.__dia == 2 or self.__dia == 3 or self.__dia == 5: valor_base = 16
        elif self.__dia == 1 or self.__dia == 6 or self.__dia == 7: valor_base = 20
        else: raise ValueError("Dia inválido")

        if 17 <= self.__hora <= 24:
            valor_base *= 1.5

        return valor_base

    
# Interface com o usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta()
            if op == 5: UI.ingresso()
    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem, 4-Conta Bancária, 5-Ingresso, 9-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")
    @staticmethod
    def circulo():
        print("Cálculo da área e circumferência de um círculo")
        x = Circulo()
        x.set_raio(float(input("Informe o raio do círculo: ")))
        area = x.calc_area()
        circumferencia = x.calc_circumferencia()
        print(f"A área de um círculo com raio {x.get_raio()} é = {area}")
        print(f"A circumferência de um círculo com raio {x.get_raio()} é = {circumferencia}")
    @staticmethod
    def viagem():
        print("Cálculo da velocidade média atingida numa viagem")
        x = Viagem()
        x.set_distancia(float(input("Informe a distância percorrida (em KM): ")))
        x.set_tempo(int(input("Informe o tempo gasto (em horas e minutos): ")))
        kmh = x.velocidade_media()
        print(f"A velocidade média atingida é de {kmh} Km/h")
    @staticmethod
    def conta():
        x = Conta()
        x.set_nome(input("Informe seu nome: "))
        x.set_numero(int(input("Informe o número da conta: ")))
        x.set_saldo(float(input("Informe seu saldo:")))
        print("1-Depositar 2-Sacar")
        op = int(input("Escolha: "))
        if op == 1:x.deposito(float(input("Valor que será depositado: ")))
        elif op == 2:x.saque(float(input("Valor que será sacado: ")))
        print(f"Saldo final: {x.get_saldo()}")
    @staticmethod
    def ingresso():
        print("Cálculo do ingresso para entrada de cinema")
        x = Ingresso()
        print("1-Domingo 2-Segunda 3-Terça 4-Quarta 5-Quinta 6-Sexta 7-Sábado")
        x.set_dia(int(input("Informe o dia da semana: ")))
        x.set_hora(float(input("Informe o horário (0-24): ")))
        print(f"Os ingressos custam R$ {x.valor()}")
UI.main()
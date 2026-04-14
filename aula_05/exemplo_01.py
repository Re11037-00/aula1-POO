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
        if d >= 0: self.__b = d
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__h = t
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo
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
        x = Circulo()
        x.set_raio(float(input("Informe o raio do círculo: ")))
        area = x.calc_area()
        circumferencia = x.calc_circumferencia()
        print(f"A área de um círculo com raio {x.get_raio()} é = {area}")
        print(f"A circumferência de um círculo com raio {x.get_raio()} é = {circumferencia}")
    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Informe a distância percorrida (em KM): ")))
        x.set_tempo(float(input("Informe o tempo gasto (em horas e minutos): ")))
        kmh = x.velocidade_media()
        print(f"A velocidade média atingida é de {kmh} Km/h")
UI.main()

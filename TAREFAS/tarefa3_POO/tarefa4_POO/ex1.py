class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)

    def set_destino(self, valor):
        self.__destino = valor
    def set_distancia(self, valor):
        if valor > 0: self.__distancia = valor
        else: raise ValueError()
    def set_litros(self, valor):
        if valor > 0: self.__litros = valor
        else: raise ValueError()

    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros
    def ToString(self):
        return f"Destino: {self.__destino} | Distância: {self.__distancia}km | Litros: {self.__litros}L"
    def __str__(self):
        return self.ToString()


class ViagemUI:
    @staticmethod
    def Menu():
        print("1 - Calcular,  2 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def Main():
        op = 0
        while op != 2:
            op = ViagemUI.Menu()
            if op == 1: ViagemUI.Calculo()
    @staticmethod
    def Calculo():
        destino = input("informe o destino: ")
        distancia = float(input("Informe a distância percorrida em KM: "))
        litros = float(input("Informe quantos litros de combustível foram consumidos: "))
        x = Viagem(destino, distancia, litros)
        print(x.ToString())
        print(f"Consumo Médio: {x.consumo():.2f} km/l")
ViagemUI.Main()
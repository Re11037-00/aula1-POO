class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def set_nome(self, valor): 
        self.__nome = valor
    def set_populacao(self, valor): 
        if valor >= 0: self.__populacao = valor
        else: raise ValueError()
    def set_area(self, valor): 
        if valor > 0: self.__area = valor
        else: raise ValueError()

    def get_nome(self): 
        return self.__nome
    def get_populacao(self): 
        return self.__populacao
    def get_area(self): 
        return self.__area
    def densidade(self):
        return self.__populacao / self.__area
    def ToString(self):
        return f"País: {self.__nome} | População: {self.__populacao} hab | Área: {self.__area} km²"
    def __str__(self):
        return self.ToString()


class PaisUI:
    @staticmethod
    def Menu():
        print("1 - Calcular,  2 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def Main():
        op = 0
        while op != 2:
            op = PaisUI.Menu()
            if op == 1: PaisUI.Calculo()
    @staticmethod
    def Calculo():
        nome = input("Informe o nome do País: ")
        populacao = int(input("Informe a sua população: "))
        area = float(input("Informe a sua área em km²: "))
        x = Pais(nome, populacao, area)
        print(x.ToString())
        print(f"Densidade Demográfica: {x.densidade():.2f} hab/km²")
PaisUI.Main()
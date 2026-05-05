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
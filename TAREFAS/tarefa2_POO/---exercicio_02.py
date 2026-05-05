'''2. Calcular a densidade de demográfica de um país usando a classe País. A classe define os atributos nome,
população e área para armazenar os dados de um país.
A classe deve ter um método para calcular a densidade demográfica do país dada pela razão entre a população e
a área do país.
Usando a classe, escreve um programa para ler os dados de 10 país do usuário e apresentar o país com a maior
densidade demográfica.'''

#2
class Pais:
    def __init__(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0
    def calc_densidade(self):
        return self.populacao / self.area
    
#País 1
x1 = Pais()
x1.nome = (input("Digite o nome do primeiro país: "))
x1.populacao = int(input("Digite sua população: "))
x1.area = int(input("Digite a área em km2:"))
x1_densidade = x1.calc_densidade()
print("--------------------------------------------------------------------")
#País 2
x2 = Pais()
x2.nome = (input("Digite o nome do segundo país: "))
x2.populacao = int(input("Digite sua população: "))
x2.area = int(input("Digite a área em km2:"))
x2_densidade = x2.calc_densidade()
print("--------------------------------------------------------------------")
#País 3
x3 = Pais()
x3.nome = (input("Digite o nome do terceiro país: "))
x3.populacao = int(input("Digite sua população: "))
x3.area = int(input("Digite a área em km2:"))
x3_densidade = x3.calc_densidade()
print("--------------------------------------------------------------------")
#País 4
x4 = Pais()
x4.nome = (input("Digite o nome do quarto país: "))
x4.populacao = int(input("Digite sua população: "))
x4.area = int(input("Digite a área em km2:"))
x4_densidade = x4.calc_densidade()
print("--------------------------------------------------------------------")
#País 5
x5 = Pais()
x5.nome = (input("Digite o nome do quinto país: "))
x5.populacao = int(input("Digite sua população: "))
x5.area = int(input("Digite a área em km2:"))
x5_densidade = x5.calc_densidade()
print("--------------------------------------------------------------------")
#País 6
x6 = Pais()
x6.nome = (input("Digite o nome do sexto país: "))
x6.populacao = int(input("Digite sua população: "))
x6.area = int(input("Digite a área em km2:"))
x6_densidade = x6.calc_densidade()
print("--------------------------------------------------------------------")
#País 7
x7 = Pais()
x7.nome = (input("Digite o nome do sétimo país: "))
x7.populacao = int(input("Digite sua população: "))
x7.area = int(input("Digite a área em km2:"))
x7_densidade = x7.calc_densidade()
print("--------------------------------------------------------------------")
#País 8
x8 = Pais()
x8.nome = (input("Digite o nome do oitavo país: "))
x8.populacao = int(input("Digite sua população: "))
x8.area = int(input("Digite a área em km2:"))
x8_densidade = x8.calc_densidade()
print("--------------------------------------------------------------------")
#País 9
x9 = Pais()
x9.nome = (input("Digite o nome do nono país: "))
x9.populacao = int(input("Digite sua população: "))
x9.area = int(input("Digite a área em km2:"))
x9_densidade = x9.calc_densidade()
print("--------------------------------------------------------------------")
#País 10
x10 = Pais()
x10.nome = (input("Digite o nome do décimo país: "))
x10.populacao = int(input("Digite sua população: "))
x10.area = int(input("Digite a área em km2:"))
x10_densidade = x10.calc_densidade()
print("--------------------------------------------------------------------")

maior_densidade = max(x1_densidade, x2_densidade, x3_densidade, x4_densidade, x5_densidade, x6_densidade, x7_densidade, x8_densidade, x9_densidade, x10_densidade)

if maior_densidade == x1_densidade:
    print(f"o país com a maior densidade demográfica é {x1.nome}")
elif maior_densidade == x2_densidade:
    print(f"o país com a maior densidade demográfica é {x2.nome}")
elif maior_densidade == x3_densidade:
    print(f"o país com a maior densidade demográfica é {x3.nome}")
elif maior_densidade == x4_densidade:
    print(f"o país com a maior densidade demográfica é {x4.nome}")
elif maior_densidade == x5_densidade:
    print(f"o país com a maior densidade demográfica é {x5.nome}")
elif maior_densidade == x6_densidade:
    print(f"o país com a maior densidade demográfica é {x6.nome}")
elif maior_densidade == x7_densidade:
    print(f"o país com a maior densidade demográfica é {x7.nome}")
elif maior_densidade == x8_densidade:
    print(f"o país com a maior densidade demográfica é {x8.nome}")
elif maior_densidade == x9_densidade:
    print(f"o país com a maior densidade demográfica é {x9.nome}")
elif maior_densidade == x10_densidade:
    print(f"o país com a maior densidade demográfica é {x10.nome}")

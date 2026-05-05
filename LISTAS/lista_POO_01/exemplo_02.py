'''Uma Viagem
A classe deve ter atributos para armazenar a distância em km e o tempo gasto em horas e minutos da viagem
realizada. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo
com a distância e o tempo gasto.
Escrever um programa para testar a classe.'''

#A classe é o modelo 
class Viagem:
    # atributo - dados que serão armazenados
    def __init__(self):
        self.distancia = 0
        self.tempo = 0
    #método -cálculos que vão ser feitos
    def calc_vel(self):
        return self.distancia / self.tempo
    

x = Viagem()
print("Informe a distância percorrida (em Km):")
x.distancia = float(input())
print("Informe o tempo gasto na viagem (em horas e minutos):")
x.tempo = float(input())
a = x.calc_vel()
print(f"A velocidade média atingida na viagem é {a:.2f}Km/h")
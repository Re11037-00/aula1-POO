'''
2. Uma Viagem
Escrever a classe Viagem de acordo com o diagrama UML apresentado abaixo. A classe deve ter atributos para
armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. A classe deve possuir
método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto,
além dos métodos de acesso para definir e recuperar os atributos.
Escrever um programa para testar a classe.
'''

class viagem:
    def __init__(self):
        self.distancia = 0
        self.tempo = 0
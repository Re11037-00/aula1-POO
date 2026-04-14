'''
1. Um Círculo
Escrever a classe Círculo de acordo com o diagrama UML apresentado abaixo. A classe deve ter um atributo raio
para armazenar a dimensão da figura e métodos para calcular sua área e sua circunferência, além dos métodos de
acesso para definir e recuperar o atributo raio.

Escrever um programa para testar a classe.
'''

class circulo:
    def __init__(self):
        self.raio = ""
    def calc_area_circ(self):
        return self.raio * 2
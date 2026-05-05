'''Um Círculo
A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua
circunferência.
Escrever um programa para testar a classe.'''

#A classe é o modelo
class Circulo:
    # atributo - dados que serão armazenados
    def __init__(self):
        self.raio = 0
    #método -cálculos que vão ser feitos
    def calc_circumferencia(self):
        return 2 * (3.14) * self.raio
    
x = Circulo()
print("Informe o valor do raio")
x.raio = float(input())
a = x.calc_circumferencia()
print(f"A circumferência do círculo é {a:.2f}")


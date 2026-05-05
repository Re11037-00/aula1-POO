import math 

class Triangulo:
 def __init__(self):
   self.__b=0.0; self.__h=0.0
 def set_base(self,v):
   if v>=0:self.__b=v
   else:raise ValueError()
 def set_altura(self,v):
   if v>=0:self.__h=v
   else:raise ValueError()
 def get_base(self):return self.__b
 def get_altura(self):return self.__h
 def calc_area(self):return self.__b*self.__h/2

class Circulo:
 def __init__(self):
  self.__raio=0.0
 def set_raio(self,v):
  if v>=0:self.__raio=v
  else:raise ValueError()
 def get_raio(self):
  return self.__raio
 def calc_area(self):
  return math.pi*self.__raio**2
 def calc_circunferencia(self):
  return 2*math.pi*self.__raio

class Viagem:
 def __init__(self):
  self.__distancia=0.0; self.__tempo=0.0
 def set_distancia(self,d):
  if d>=0:self.__distancia=d
  else:raise ValueError()
 def set_tempo(self,t):
  if t>0:self.__tempo=t
  else:raise ValueError()
 def get_distancia(self):return self.__distancia
 def get_tempo(self):return self.__tempo
 def velocidade_media(self):return self.__distancia/self.__tempo

class Conta:
 def __init__(self):
  self.__nome=""; self.__numero=0; self.__saldo=0.0
 def set_nome(self,n):self.__nome=n
 def set_numero(self,v):
  if v>=0:self.__numero=v
  else:raise ValueError()
 def set_saldo(self,s):self.__saldo=s
 def get_nome(self):return self.__nome
 def get_numero(self):return self.__numero
 def get_saldo(self):return self.__saldo
 def deposito(self,valor):
  if valor>0:self.__saldo+=valor
  else:raise ValueError()
 def saque(self,valor):
  if 0 < valor <= self.__saldo: self.__saldo -= valor
  else:raise ValueError()

class Ingresso:
 def __init__(self):
  self.__dia = 0
  self.__hora = 0
 def set_dia(self,d):
  if 1 <= d <= 7: self.__dia = d
  else: raise ValueError()
 def set_hora(self,h):
  if 0<=h<=24:self.__hora=h
  else:raise ValueError()
 def get_dia(self):return self.__dia
 def get_hora(self):return self.__hora
 def valor(self):
  if self.__dia==4:return 8
  if self.__dia in [2,3,5]:valor_base=16
  else:valor_base=20
  if 17<=self.__hora<=24:valor_base*=1.5
  return valor_base

class UI:
 @staticmethod
 def main():
  op = 0
  while op != 9:
    op = UI.menu()
    if op == 1:UI.triangulo()
    if op == 2:UI.circulo()
    if op == 3:UI.viagem()
    if op == 4:UI.conta()
    if op == 5:UI.ingresso()
 
 @staticmethod
 def menu():
  print("1-Triângulo 2-Círculo 3-Viagem 4-Conta 5-Ingresso 9-Fim")
  return int(input("Escolha: "))
 
 @staticmethod
 def triangulo():
  x = Triangulo()
  x.set_base(float(input("Base: ")))
  x.set_altura(float(input("Altura: ")))
  print(f"Área = {x.calc_area()}")
 
 @staticmethod
 def circulo():
  x=Circulo()
  x.set_raio(float(input("Raio: ")))
  print("Área =",x.calc_area())
  print("Circunferência =",x.calc_circunferencia())
 
 @staticmethod
 def viagem():
  x=Viagem()
  x.set_distancia(float(input("Distância: ")))
  x.set_tempo(float(input("Tempo: ")))
  print("Velocidade =",x.velocidade_media(),"km/h")
 
 @staticmethod
 def conta():
  x=Conta()
  x.set_nome(input("Nome: "))
  x.set_numero(int(input("Conta: ")))
  x.set_saldo(float(input("Saldo: ")))
  print("1-Depositar 2-Sacar")
  op=int(input("Escolha: "))
  if op==1:x.deposito(float(input("Valor: ")))
  elif op==2:x.saque(float(input("Valor: ")))
  print("Saldo final:",x.get_saldo())
  
 @staticmethod
 def ingresso():
  x=Ingresso()
  print("1-Dom 2-Seg 3-Ter 4-Qua 5-Qui 6-Sex 7-Sab")
  x.set_dia(int(input("Dia: ")))
  x.set_hora(float(input("Hora: ")))
  print("Valor =",x.valor())

UI.main()
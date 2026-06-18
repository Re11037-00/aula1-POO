from datetime import timedelta, datetime

class Treino:
    def __init__(self, id, data, dist, t):
        self.set_id(id) #int
        self.set_data(data) #datetime
        self.set_distancia(dist) #double
        self.set_tempo(t) #timedelta

    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_data(self, data): #datetime
        if data == "": raise ValueError("Data não pode ser vazia")
        self.__data = data
    def set_distancia(self, dist):
        if dist < 0: raise ValueError("Distância deve ser positiva")
        self.__distancia = dist
    def set_tempo(self, t):
        if t < timedelta(0): raise ValueError("Tempo deve ser positivo")
        self.__tempo = t

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo

    def pace(self): #Inserir o método Pace para calcula o pace da corrida que mede o tempo gasto para correr um quilometro;
        pass
        # return  / self.__distancia / 60 #minutos por km

    def __str__(self): 
         return f" id: {self.__id} | data: {self.__data} | distância: {self.__distancia} | tempo: {self.__tempo}"

class TreinoUI:
   __treino = []        #atributo -  fora do init - não tem objetos de pacienteUI

@staticmethod           #quando não acessa o atributo
def Main():
    opcao = 0
    while opcao != 9:
        opcao = TreinoUI.Menu()
        if opcao == 1: TreinoUI.Inserir()
        if opcao == 2: TreinoUI.Listar()
        if opcao == 3: TreinoUI.Listar_id()
        if opcao == 4: TreinoUI.Atualizar()
        if opcao == 5: TreinoUI.Excluir()
        if opcao == 6: TreinoUI.MaisRapido()
        if opcao == 9:
            print('Saindo...')
            break
        else: print('Opção inválida.')

@staticmethod
def Menu():
        print("1-Inserir treinos 2-Listar treinos 3-Listar treino por ID 4-Atualizar treino 5-Excluir treino 6-Treino mais rápido")
        print("9-fim")
        return int(input("Escolha uma opção: "))
    
@classmethod 
def Inserir(cls):
       pass #Inserir, para inserir um treino na lista;
    
@classmethod
def Listar(cls):
       pass #Listar, para listar todos os treinos do atleta;
@classmethod
def Listar_id(cls):
       pass #Listar_Id, para listar o treino com um determinado id;

@classmethod
def Atualizar(cls):
       pass #Atualizar, para atualizar os dados de um treino;
               
@classmethod
def pesquisar(cls):
       pass #Excluir, para excluir um treino da lista;
        
@classmethod
def MaisRapido(cls):
       pass #MaisRapido, para mostrar o treino em que o atleta obteve a maior velocidade média, ou seja, o menor pace.

TreinoUI.main()

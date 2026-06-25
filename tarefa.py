from enum import Enum

class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12

class Fase(Enum):
    Grupos = 1
    DezesseisAvos = 2
    Oitavas = 3
    Quartas = 4
    Semifinais = 5
    TerceiroLugar = 6
    Final = 7

class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)

    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_sigla(self, sigla):
        if sigla == "": raise ValueError("Sigla não pode ser vazia")
        self.__sigla = sigla
    # def set_grupo(self, grupo):
    #     if grupo == "": raise ValueError("Telefone não pode ser vazio")
    #     self.__grupo = grupo
    

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_sigla(self): return self.__sigla
    # def get_grupo(self): return self.__grupo
    
       
        
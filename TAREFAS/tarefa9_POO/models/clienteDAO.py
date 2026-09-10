from Avaliação.projeto.models.cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj):
        self.__objetos.append(obj)
        self.__salvar()
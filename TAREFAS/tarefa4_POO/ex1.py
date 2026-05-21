# class Time
# class Jogadores
# class UI

class Times:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_id(self, valor):
        if valor <= 0: raise ValueError("ID inválido")
        else: self.__id = valor

    def set_nome(self, valor):
        self.__nome = valor

    def set_estado(self, valor):
        self.__estado = valor
        

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def ToString(self):
        return f" id: {self.__id} | nome do time: {self.__nome} | estado: {self.__estado}"
    def __str__(self):
        return self.ToString()


class Jogadores:
    def __init__(self, id, id_time, nome, camisa):
        self.set_id(id)
        self.set_time(id_time)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self, valor):
        if valor <= 0: raise ValueError("ID inválido")
        else: self.__id = valor

    def set_time(self, valor):
        self.__id_time = valor

    def set_nome(self, valor):
        self.__nome = valor

    def set_camisa(self, valor):
        self.__camisa = valor
        
    def get_id(self):
        return self.__id
    def get_time(self):
        return self.__id_time
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def ToString(self):
        return f" id: {self.__id} | id do time: {self.__id_time} | nome: {self.__nome} | camisa: {self.__camisa}"
    def __str__(self):
        return self.ToString()

class UI:
    times = []
    jogadores = []

    @staticmethod
    def Main():
         while True:
            opcao = UI.Menu()
            if opcao == 1:
                UI.inserir_time()
            elif opcao == 2:
                UI.listar_time()
            elif opcao == 3:
                UI.atualizar_time()
            elif opcao == 4:
                UI.excluir_time()
            elif opcao == 5:
                UI.inserir_jogador()
            elif opcao == 6:
                UI.listar_jogador()
            elif opcao == 7:
                UI.atualizar_jogador()
            elif opcao == 8:
                UI.excluir_jogador()
            elif opcao == 9:
                UI.listar_jogadores_do_time()
            elif opcao == 10:
                UI.transferir_jogador()
            elif opcao == 11:
                print('Saindo...')
                break
            else:
                print('Opção inválida.')

    @staticmethod
    def Menu():
        print("1-Inserir times 2-Listar times 3-Atualizar times 4-Excluir times")
        print("5-Inserir jogadores 6-Listar jogadores 7-Atualizar jogadores 8-Excluir jogadores")
        print("9 - Listar jogadores do time 10 - Transferir jogador 11 - Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def inserir_time():
        print("Inserir Time:")
        id = int(input("Informe o id do time: "))
        nome = input("Informe o nome do time: ")
        estado = input("Informe o estado do time: ")
        time = Times(id, nome, estado)
        UI.times.append(time)
        print("Time inserido com sucesso!")

    @staticmethod
    def listar_time():
        print("Lista de Times:")
        if len(UI.times) == 0:
            print("Nenhum time cadastrado.")
        else:
            for time in UI.times:
                print(time)
    
    @staticmethod
    def atualizar_time():
        print("Atualizar Time:")
        id = int(input("Informe o id do time a ser atualizado: "))
        for time in UI.times:
            if time.get_id() == id:
                nome = input("Informe o novo nome do time: ")
                estado = input("Informe o novo estado do time: ")
                time.set_nome(nome)
                time.set_estado(estado)
                print("Time atualizado com sucesso!")
                return
        print("Time não encontrado.")
    
    @staticmethod
    def excluir_time():
        print("Excluir Time:")
        id = int(input("Informe o id do time a ser excluído: "))
        for time in UI.times:
            if time.get_id() == id:
                UI.times.remove(time)
                print("Time excluído com sucesso!")
                return
        print("Time não encontrado.")
    


    @staticmethod
    def inserir_jogador():
        print("Inserir Jogador:")
        id = int(input("Informe o id do jogador: "))
        id_time = int(input("Informe o id do time do jogador: "))
        nome = input("Informe o nome do jogador: ")
        camisa = input("Informe a camisa do jogador: ")
        jogador = Jogadores(id, id_time, nome, camisa)
        UI.jogadores.append(jogador)
        print("Jogador inserido com sucesso!")
    
    @staticmethod
    def listar_jogador():
        print("Lista de Jogadores:")
        if len(UI.jogadores) == 0:
            print("Nenhum jogador cadastrado.")
        else:
            for jogador in UI.jogadores:
                print(jogador)
    
    @staticmethod
    def atualizar_jogador():
        print("Atualizar Jogador:")
        id = int(input("Informe o id do jogador a ser atualizado: "))
        for jogador in UI.jogadores:
            if jogador.get_id() == id:
                id_time = int(input("Informe o novo id do time do jogador: "))
                nome = input("Informe o novo nome do jogador: ")
                camisa = input("Informe a nova camisa do jogador: ")
                jogador.set_time(id_time)
                jogador.set_nome(nome)
                jogador.set_camisa(camisa)
                print("Jogador atualizado com sucesso!")
                return
        print("Jogador não encontrado.")
    
    @staticmethod
    def excluir_jogador():
        print("Excluir Jogador:")
        id = int(input("Informe o id do jogador a ser excluído: "))
        for jogador in UI.jogadores:
            if jogador.get_id() == id:
                UI.jogadores.remove(jogador)
                print("Jogador excluído com sucesso!")
                return
        print("Jogador não encontrado.")    
    
    @staticmethod
    def listar_jogadores_do_time():
        print("Listar Jogadores do Time:")
        id_time = int(input("Informe o id do time: "))
        jogadores_do_time = [jogador for jogador in UI.jogadores if jogador.get_time() == id_time]
        if len(jogadores_do_time) == 0:
            print("Nenhum jogador encontrado para esse time.")
        else:
            for jogador in jogadores_do_time:
                print(jogador)
    
    @staticmethod
    def transferir_jogador():
        print("Transferir Jogador:")
        id_jogador = int(input("Informe o id do jogador a ser transferido: "))
        jogador = next((j for j in UI.jogadores if j.get_id() == id_jogador), None)
        if jogador is None:
            print("Jogador não encontrado.")
            return
        
        novo_id_time = int(input("Informe o id do novo time: "))
        if not any(time.get_id() == novo_id_time for time in UI.times):
            print("Time não encontrado.")
            return
        
        jogador.set_time(novo_id_time)
        print("Jogador transferido com sucesso!")
    
    @staticmethod
    def find_time(id_time):
        for time in UI.times:
            if time.get_id() == id_time:
                return time
        return None
    
    @staticmethod
    def find_jogador(id_jogador):
        for jogador in UI.jogadores:
            if jogador.get_id() == id_jogador:
                return jogador
        return None
  
UI.Main()
    
    #     x = 0
    #     while x != 2:
    #         x = UI.Menu()
    #         if x == 1: UI.Menu()
    #     print("1 - Menu,  2 - Sair")
    #     return int(input("Escolha uma opção: "))
    # @staticmethod
    # def Menu():
#         op = 0
#         while op != 9:
#             op = UI.Menu()
#             if op == 1: UI.inserir_time()   
#             if op == 2: UI.listar_time()    
#             if op == 3: UI.atualizar_time() 
#             if op == 4: UI.excluir_time()   
#             if op == 5: UI.inserir_jogador()   
#             if op == 6: UI.listar_jogador()    
#             if op == 7: UI.atualizar_jogador() 
#             if op == 8: UI.excluir_jogador()   
#         print("1-Inserir times 2-Listar times 3-Atualizar times 4-Excluir times")
#         print("5-Inserir jogadores 6-Listar jogadores 7-Atualizar jogadores 8-Excluir jogadores")
#         print("9 - fim")
#         op = int(input("Informe uma opção: ")) 
   
# UI.Main()
#     # @staticmethod
#     # def Calculo():
#     #     id = int(input("informe o id do time : "))
#     #     nome = input("Informe o nome do time: ")
#     #     estado = (input("Informe o estado: ")
#     #     x =Times(id, nome, estado)
#     #     print(x.ToString())
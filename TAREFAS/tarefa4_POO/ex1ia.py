# Classe Time, Jogador e UI para gerenciar times e jogadores de futebol
# UML simples:
# Time(id, nome, estado)
# Jogador(id, nome, camisa, id_time)
# UI(times, jogadores, menu, operações CRUD e transferência)

class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)

    def set_id(self, valor):
        if valor <= 0:
            raise ValueError('O id do time deve ser maior que zero.')
        self.__id = valor

    def set_nome(self, valor):
        self.__nome = str(valor).strip()

    def set_estado(self, valor):
        self.__estado = str(valor).strip()


    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_estado(self):
        return self.__estado

    def ToString(self):
        return f"id: {self.__id} | nome: {self.__nome} | estado: {self.__estado}"

    def __str__(self):
        return self.ToString()


class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.set_id(id)
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_id_time(id_time)

    def set_id(self, valor):
        if valor <= 0:
            raise ValueError('O id do jogador deve ser maior que zero.')
        self.__id = valor

    def set_nome(self, valor):
        self.__nome = str(valor).strip()

    def set_camisa(self, valor):
        if valor <= 0:
            raise ValueError('O número da camisa deve ser maior que zero.')
        self.__camisa = valor

    def set_id_time(self, valor):
        self.__id_time = valor

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_camisa(self):
        return self.__camisa

    def get_id_time(self):
        return self.__id_time

    def ToString(self):
        return (
            f"id: {self.__id} | nome: {self.__nome} | camisa: {self.__camisa} "
            f"| id do time: {self.__id_time}"
        )

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
                print('Opção inválida. Tente novamente.')

    @staticmethod
    def Menu():
        print('\n=== Menu de Cadastro de Times e Jogadores ===')
        print('1 - Inserir time')
        print('2 - Listar times')
        print('3 - Atualizar time')
        print('4 - Excluir time')
        print('5 - Inserir jogador')
        print('6 - Listar jogadores')
        print('7 - Atualizar jogador')
        print('8 - Excluir jogador')
        print('9 - Listar jogadores de um time')
        print('10 - Transferir jogador')
        print('11 - Sair')
        return UI.read_int('Escolha uma opção: ')

    @staticmethod
    def inserir_time():
        print('\n--- Inserir Time ---')
        id_time = UI.read_int('Informe o id do time: ')
        if UI.find_time(id_time) is not None:
            print('Já existe um time cadastrado com esse id.')
            return

        nome = input('Informe o nome do time: ').strip()
        estado = input('Informe o estado do time: ').strip()
        UI.times.append(Time(id_time, nome, estado))
        print('Time inserido com sucesso.')

    @staticmethod
    def listar_time():
        print('\n--- Lista de Times ---')
        if not UI.times:
            print('Nenhum time cadastrado.')
            return

        for time in UI.times:
            print(time.ToString())

    @staticmethod
    def atualizar_time():
        print('\n--- Atualizar Time ---')
        id_time = UI.read_int('Informe o id do time a ser atualizado: ')
        time = UI.find_time(id_time)
        if time is None:
            print('Time não encontrado.')
            return

        nome = input(f'Nome atual ({time.get_nome()}): ').strip()
        estado = input(f'Estado atual ({time.get_estado()}): ').strip()
        if nome:
            time.set_nome(nome)
        if estado:
            time.set_estado(estado)
        print('Time atualizado com sucesso.')

    @staticmethod
    def excluir_time():
        print('\n--- Excluir Time ---')
        id_time = UI.read_int('Informe o id do time a ser excluído: ')
        time = UI.find_time(id_time)
        if time is None:
            print('Time não encontrado.')
            return

        if any(jogador.get_id_time() == id_time for jogador in UI.jogadores):
            print('Não é possível excluir o time enquanto existem jogadores associados a ele.')
            return

        UI.times.remove(time)
        print('Time excluído com sucesso.')

    @staticmethod
    def inserir_jogador():
        print('\n--- Inserir Jogador ---')
        id_jogador = UI.read_int('Informe o id do jogador: ')
        if UI.find_jogador(id_jogador) is not None:
            print('Já existe um jogador cadastrado com esse id.')
            return

        nome = input('Informe o nome do jogador: ').strip()
        camisa = UI.read_int('Informe o número da camisa: ')
        id_time = UI.read_int('Informe o id do time onde o jogador atua: ')
        if UI.find_time(id_time) is None:
            print('Time não encontrado. Cadastre o time antes de inserir o jogador.')
            return

        UI.jogadores.append(Jogador(id_jogador, nome, camisa, id_time))
        print('Jogador inserido com sucesso.')

    @staticmethod
    def listar_jogador():
        print('\n--- Lista de Jogadores ---')
        if not UI.jogadores:
            print('Nenhum jogador cadastrado.')
            return

        for jogador in UI.jogadores:
            print(jogador.ToString())

    @staticmethod
    def atualizar_jogador():
        print('\n--- Atualizar Jogador ---')
        id_jogador = UI.read_int('Informe o id do jogador a ser atualizado: ')
        jogador = UI.find_jogador(id_jogador)
        if jogador is None:
            print('Jogador não encontrado.')
            return

        nome = input(f'Nome atual ({jogador.get_nome()}): ').strip()
        camisa_input = input(f'Camisa atual ({jogador.get_camisa()}): ').strip()
        id_time_input = input(f'Id do time atual ({jogador.get_id_time()}): ').strip()

        if nome:
            jogador.set_nome(nome)
        if camisa_input:
            try:
                camisa = int(camisa_input)
                jogador.set_camisa(camisa)
            except ValueError:
                print('Número da camisa inválido. Mantendo o valor atual.')
        if id_time_input:
            try:
                novo_time = int(id_time_input)
                if UI.find_time(novo_time) is None:
                    print('Time não encontrado. Mantendo o time atual.')
                else:
                    jogador.set_id_time(novo_time)
            except ValueError:
                print('Id do time inválido. Mantendo o time atual.')

        print('Jogador atualizado com sucesso.')

    @staticmethod
    def excluir_jogador():
        print('\n--- Excluir Jogador ---')
        id_jogador = UI.read_int('Informe o id do jogador a ser excluído: ')
        jogador = UI.find_jogador(id_jogador)
        if jogador is None:
            print('Jogador não encontrado.')
            return

        UI.jogadores.remove(jogador)
        print('Jogador excluído com sucesso.')

    @staticmethod
    def listar_jogadores_do_time():
        print('\n--- Jogadores de um Time ---')
        id_time = UI.read_int('Informe o id do time: ')
        time = UI.find_time(id_time)
        if time is None:
            print('Time não encontrado.')
            return

        jogadores_do_time = [j for j in UI.jogadores if j.get_id_time() == id_time]
        if not jogadores_do_time:
            print('Nenhum jogador cadastrado para este time.')
            return

        print(f'Jogadores do time {time.get_nome()} (id {time.get_id()}):')
        for jogador in jogadores_do_time:
            print(jogador.ToString())

    @staticmethod
    def transferir_jogador():
        print('\n--- Transferir Jogador ---')
        id_jogador = UI.read_int('Informe o id do jogador a ser transferido: ')
        jogador = UI.find_jogador(id_jogador)
        if jogador is None:
            print('Jogador não encontrado.')
            return

        novo_id_time = UI.read_int('Informe o id do novo time: ')
        novo_time = UI.find_time(novo_id_time)
        if novo_time is None:
            print('Time de destino não encontrado.')
            return

        jogador.set_id_time(novo_id_time)
        print('Jogador transferido com sucesso.')

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

    @staticmethod
    def read_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print('Valor inválido. Informe um número inteiro.')


if __name__ == '__main__':
    UI.Main()
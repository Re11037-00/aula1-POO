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

    def pace(self):
        # Calcula o total de minutos e divide pela distância em km
        if self.__distancia == 0: return 0
        total_minutos = self.__tempo.total_seconds() / 60
        return total_minutos / self.__distancia

    def __str__(self): 
         data_formatada = self.__data.strftime('%d/%m/%Y')
         return f"id: {self.__id} | data: {data_formatada} | distância: {self.__distancia}km | tempo: {self.__tempo} | pace: {self.pace():.2f} min/km"


class TreinoUI:
    __treino = [] # Lista que armazenará os objetos da classe Treino

    @staticmethod           
    def main():
        opcao = 0
        while opcao != 9:
            opcao = TreinoUI.Menu()
            if opcao == 1: TreinoUI.Inserir()
            elif opcao == 2: TreinoUI.Listar()
            elif opcao == 3: TreinoUI.Listar_id()
            elif opcao == 4: TreinoUI.Atualizar()
            elif opcao == 5: TreinoUI.Excluir()
            elif opcao == 6: TreinoUI.MaisRapido()
            elif opcao == 9:
                print('Saindo...')
                break
            else: 
                print('Opção inválida.\n')

    @staticmethod
    def Menu():
        print("\n--- MENU TREINOS ---")
        print("1-Inserir treino | 2-Listar treinos | 3-Listar por ID")
        print("4-Atualizar treino | 5-Excluir treino | 6-Treino mais rápido")
        print("9-Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0
        
    @classmethod 
    def Inserir(cls):
        print("\n-- Inserir Treino --")
        try:
            id = int(input("ID do treino: "))
            # Validação simples para evitar IDs duplicados
            for t in cls.__treino:
                if t.get_id() == id:
                    print("Erro: Já existe um treino com este ID.")
                    return
            
            data_str = input("Data (DD/MM/AAAA): ")
            data = datetime.strptime(data_str, "%d/%m/%Y")
            
            dist = float(input("Distância (km): "))
            
            tempo_str = input("Tempo (HH:MM:SS): ")
            h, m, s = map(int, tempo_str.split(':'))
            t = timedelta(hours=h, minutes=m, seconds=s)
            
            novo_treino = Treino(id, data, dist, t)
            cls.__treino.append(novo_treino)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir treino: {e}")
        
    @classmethod
    def Listar(cls):
        print("\n-- Lista de Treinos --")
        if not cls.__treino:
            print("Nenhum treino cadastrado.")
            return
        for t in cls.__treino:
            print(t)

    @classmethod
    def Listar_id(cls):
        print("\n-- Buscar Treino por ID --")
        id = int(input("Digite o ID do treino: "))
        for t in cls.__treino:
            if t.get_id() == id:
                print(t)
                return
        print("Treino não encontrado.")

    @classmethod
    def Atualizar(cls):
        print("\n-- Atualizar Treino --")
        id = int(input("Digite o ID do treino que deseja atualizar: "))
        for t in cls.__treino:
            if t.get_id() == id:
                try:
                    data_str = input("Nova Data (DD/MM/AAAA): ")
                    data = datetime.strptime(data_str, "%d/%m/%Y")
                    dist = float(input("Nova Distância (km): "))
                    tempo_str = input("Novo Tempo (HH:MM:SS): ")
                    h, m, s = map(int, tempo_str.split(':'))
                    tempo = timedelta(hours=h, minutes=m, seconds=s)
                    
                    t.set_data(data)
                    t.set_distancia(dist)
                    t.set_tempo(tempo)
                    print("Treino atualizado com sucesso!")
                    return
                except Exception as e:
                    print(f"Erro ao atualizar: {e}")
                    return
        print("Treino não encontrado.")
            
    @classmethod
    def Excluir(cls):
        print("\n-- Excluir Treino --")
        id = int(input("Digite o ID do treino que deseja remover: "))
        for t in cls.__treino:
            if t.get_id() == id:
                cls.__treino.remove(t)
                print("Treino excluído com sucesso!")
                return
        print("Treino não encontrado.")
            
    @classmethod
    def MaisRapido(cls):
        print("\n-- Treino Mais Rápido (Menor Pace) --")
        if not cls.__treino:
            print("Nenhum treino cadastrado.")
            return
        
        # O treino mais rápido é o que tem o MENOR pace
        mais_rapido = min(cls.__treino, key=lambda t: t.pace())
        print("O treino com melhor rendimento foi:")
        print(mais_rapido)

# Inicializa o programa
TreinoUI.main()
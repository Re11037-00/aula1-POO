from datetime import datetime

class Paciente:

    def __init__(self, id, n, c, t, nasc):
        self.set_id(id)
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nascimento(nasc)

    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_nome(self, n):
        if n == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = n
    def set_cpf(self, c):
        if c == "": raise ValueError("CPF não pode ser vazio")
        self.__cpf = c
    def set_telefone(self, t):
        if t == "": raise ValueError("Telefone não pode ser vazio")
        self.__telefone = t
    def set_nascimento(self, nasc):
      if nasc > datetime.now(): raise ValueError("Data de nascimento não pode ser no futuro")
      self.__nascimento = nasc 

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f" id: {self.__id} | nome: {self.__nome} | cpf: {self.__cpf} | telefone: {self.__telefone} | nascimento: {self.__nascimento}" + \
            f"{self.__nascimento.strftime('%d/%m/%Y')}"
    
    def idade(self):
        tempo = datetime.now() - self.__nascimento # medido em dias, horas, ... timedelta
        anos = tempo.days // 365
        meses = (tempo.days % 365) // 30
        return f"{anos} ano(s) e {meses} mês(es)"


class PacienteUI:
    __pacientes = [] #atributo -  fora do init - não tem objetos de pacienteUI

    @staticmethod #quando não acessa o atributo
    def Main():
         opcao = 0
         while opcao != 9:
            opcao = PacienteUI.Menu()
            if opcao == 1: PacienteUI.inserir()
            elif opcao == 2: PacienteUI.listar()
            elif opcao == 3: PacienteUI.atualizar()
            elif opcao == 4: PacienteUI.excluir()
            elif opcao == 5: PacienteUI.pesquisar()
            elif opcao == 6: PacienteUI.aniversariantes()
            elif opcao == 9:
                print('Saindo...')
                break
            else:
                print('Opção inválida.')

    @staticmethod
    def Menu():
        print("1-Inserir pacientes 2-Listar pacientes 3-Atualizar pacientes 4-Excluir pacientes 5-Pesquisar pacientes 6-Aniversariantes")
        print("9-fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod #quando acessa o atributo - usa o cls
    def inserir(cls):
        id = int(input("informe o id: "))
        nome = input("informe o nome: ")
        cpf = input("informe o CPF: ")
        fone = input("informe o telefone: ")
        nasc = datetime.strptime(input("informe a data de nascimento em formato dd/mm/yyyy: "), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, fone, nasc)
        cls.__pacientes.append(x)
    
    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado.")
        else:
            for x in cls.__pacientes: print(x, x.idade())
                
    # @classmethod
    # def atualizar(cls):

    # @classmethod
    # def excluir(cls):

    # @classmethod
    # def pesquisar(cls):

    # @classmethod
    # def aniversariantes(cls):
    

PacienteUI.Main()

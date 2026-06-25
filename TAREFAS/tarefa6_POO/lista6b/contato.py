from datetime import datetime
import json

class Contato:

    def __init__(self, id, n, e, f, nasc):
        self.set_id(id)
        self.set_nome(n)
        self.set_email(e)
        self.set_fone(f)
        self.set_nascimento(nasc)

    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_nome(self, n):
        if n == "": raise ValueError("Nome deve ser informado.")
        self.__nome = n
    def set_email(self, e):
        if e == "": raise ValueError("E-mail deve ser informado.")
        self.__email = e
    def set_fone(self, f):
        if f == "": raise ValueError("Telefone deve ser informado.")
        self.__fone = f
    def set_nascimento(self, nasc):
      if nasc > datetime.now(): raise ValueError("Data de nascimento não pode ser no futuro")
      self.__nascimento = nasc 

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        nasc_str = self.__nascimento.strftime("%d/%m/%Y")
        return f" id: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Telefone: {self.__fone} | Nascimento: {nasc_str}"

    def to_json(self):
        return { "id": self.__id, "nome": self.__nome, "email": self.__email, "fone":self.__fone, "nascimento" : self.__nascimento.strftime("%d/%m/%Y")}

    @staticmethod
    def from_json(dic):
        nasc_dt = datetime.strptime(dic["nascimento"], "%d/%m/%Y")
        return Contato(dic["id"], dic["nome"], dic["email"], dic["fone"], nasc_dt)


class ContatoUI:
    __contatos = []        #atributo -  fora do init - não tem objetos de pacienteUI

    @staticmethod           #quando não acessa o atributo
    def main():
         ContatoUI.abrir()
         opcao = 0
         while opcao != 9:
            opcao = ContatoUI.menu()
            if opcao == 1: ContatoUI.inserir()
            if opcao == 2: ContatoUI.listar()
            if opcao == 3: ContatoUI.listar_id()
            if opcao == 4: ContatoUI.atualizar()
            if opcao == 5: ContatoUI.excluir()
            if opcao == 6: ContatoUI.pesquisar()
            if opcao == 7: ContatoUI.aniversariantes()
            if opcao == 9:
                print('Saindo...')
                break

    @staticmethod
    def menu():
        print("---------------------------------------------")
        print(" 1-Inserir | 2-Listar |3-Listar id           ")
        print(" 4-Atualizar |  5-Excluir                    ")
        print(" 6-Pesquisar | 7- Aniversariantes            ")
        print(" 9-Fim                                       ")
        print("---------------------------------------------")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def salvar(cls):    
        arquivo = open("contatos.json", mode = "w")
        json.dump(cls.__contatos, arquivo, default = Contato.to_json, indent = 2)
        arquivo.close()
        print("O arquivo contatos.json foi salvo")

    @classmethod
    def abrir(cls):
        try:        
            arquivo = open("contatos.json", mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            cls.__contatos = []
            for dic in list_dic:
                x = Contato.from_json(dic)
                cls.__contatos.append(x)
            print("O arquivo contatos.json foi aberto")
        except FileNotFoundError: # Acontece qdo o arquivo não existe
            pass                  # não faz nada
    
    @classmethod #quando acessa o atributo - usa o cls
    def inserir(cls):
        id = int(input("informe o id: "))
        n = input("informe o nome: ")
        e = input("informe o e-mail: ")
        f = input("informe o telefone: ")
        nasc = datetime.strptime(input("informe a data de nascimento em formato dd/mm/yyyy: "), "%d/%m/%Y")
        x = Contato(id, n, e, f, nasc)
        cls.__contatos.append(x)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0: print("Nenhum contato cadastrado.")
        else:
            for x in cls.__contatos: print(x)

    @classmethod
    def listar_id(cls):
        try:
            id_busca = int(input("Digite o ID do contato: "))
            contato_encontrado = None
            for x in cls.__contatos:
                if x.get_id() == id_busca:
                    contato_encontrado = x
                    break
            
            if contato_encontrado: 
                print(f"Contato correspondente ao ID {id_busca}:")
                print(f"Nome: {contato_encontrado.get_nome()} | E-mail: {contato_encontrado.get_email()} | Telefone: {contato_encontrado.get_fone()} | Nascimento: {contato_encontrado.get_nascimento().strftime('%d/%m/%Y')}")
            else:
                print(f"Aviso: Nenhum contato encontrado com o ID {id_busca}.")
        except ValueError:
            print("Erro: O ID informado deve ser um número inteiro válido.")

    @classmethod
    def atualizar(cls):
        cls.listar
        if len(cls.__contatos) == 0: return
        id = int(input("Informe o id do contato a ser atualizado: "))
        encontrado = False
        for x in cls.__contatos: 
            if x.get_id() == id:
                n = input("Informe o novo nome: ")
                e = input("Informe o novo E-mail: ")
                f = input("Informe o novo telefone: ")
                nasc = datetime.strptime(input("Informe a nova data de nascimento em formato dd/mm/yyyy: "), "%d/%m/%Y")
                x.set_nome(n)
                x.set_email(e)
                x.set_fone(f)
                x.set_nascimento(nasc)
                cls.salvar()
                encontrado = True
                print("Contato atualizado com sucesso.")

    @classmethod
    def excluir(cls):
        cls.listar
        if len(cls.__contatos) == 0: return
        id = int(input("Informe o id do contato a ser excluído: "))
        encontrado = False
        for x in cls.__contatos: 
            if x.get_id() == id:
                cls.__contatos.remove(x)
                cls.salvar()
                print("Contato excluído com sucesso.")
                encontrado = True
                break
        if not encontrado: print("Contato não encontrado.")
               
    @classmethod
    def pesquisar(cls):
        s = (input("informe as iniciais do nome do contato: "))
        encontrado = False
        for x in cls.__contatos:
            if x.get_nome().startswith(s): 
                print(x)
                encontrado = True
        if not encontrado:
            print("Nenhum contato encontrado com essas iniciais.")

    @classmethod
    def aniversariantes(cls):
        try:
            m = int(input("informe o mês para a lista de aniversariantes (1-12): "))
            encontrado = False
            for x in cls.__contatos:
                if x.get_nascimento().month == m: 
                    print(x)
                    encontrados = True
                if not encontrado:
                    print("Nenhum aniversariante neste mês")
        except ValueError:
            print("Mês inválido")


ContatoUI.main()

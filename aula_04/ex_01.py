# Entidades
class Aluno:
    def __init__(self):
        self.__nome = ""      # atributos escondidos
        self.__matricula = "" # atributo encapsulado
    def set_nome(self, valor):
        if len(valor) < 3: raise ValueError("Nome deve ter pelo menos 2 letras")
        self.__nome =  valor
    def get_nome(self):
        return self.__nome
    def set_matricula(self, valor):
        if len(valor) < 5: raise ValueError("Matrícula deve ter pelo menos 5 caracteres")
        self.__matricula =  valor
    def get_matricula(self):
        return self.__matricula
    def ano_ingresso(self):        #método
        return int(self.__matricula[:4])

#programa principal
class UI:
    def main():
        x = Aluno()
        #x.nome = input("informe o nome: ")
        x.set_nome(input("informe o nome: "))
        #x.matricula = input("informe a matrícula: ")
        x.set_matricula(input("informe a matrícula: "))
        ano = x.ano_ingresso()
        print(f"O aluno {x.get_nome()}, de matrícula {x.get_matricula()}")
        print(f"Entrou no IF em {ano}")
        
UI.main()



'''
class Aluno:
    def __init__(self):
        self.__nome = ""      #atributos escondidos
        self.__matricula = ""
    def ano_ingresso(self):        
        return int(self.__matricula[:4])

#programa principal
x = Aluno()
x.nome = input("informe o nome: ")
x.matricula(input("informe a matricula: "))
ano = x.ano_ingresso
print(ano)
'''
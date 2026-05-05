#Ler uma frase e mostrar cada uma de suas palavras separadamente e de trás para frente.

print("Digite uma frase: ")
s = input()
lista = s.split()
for palavra in lista:
    print(palavra[::-1])


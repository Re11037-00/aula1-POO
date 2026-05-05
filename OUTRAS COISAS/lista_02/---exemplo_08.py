#Ler uma frase e mostrar as strings obtidas a partir desta, passando uma a uma a letra inicial para o final, até que a frase inicial seja apresentada.

frase = input("Digite uma frase: ")

for i in range(len(frase)):
 print(frase)
 frase = frase[1:] + frase[0]
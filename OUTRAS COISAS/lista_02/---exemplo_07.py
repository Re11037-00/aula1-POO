#Ler uma frase e mostrar as strings obtidas a partir desta, removendo uma a uma a palavra no início.

frase = input("Digite uma frase: ")
palavras = frase.split()
for i in range (len(palavras)):
 for j in range(i, len(palavras)):
  print(palavras[j], end=" ")
 print()
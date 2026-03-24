frase = input("Digite uma frase: ")
palavras = frase.split()
for i in range (len(palavras)):
 for j in range(i, len(palavras)):
  print(palavras[j], end=" ")
 print()
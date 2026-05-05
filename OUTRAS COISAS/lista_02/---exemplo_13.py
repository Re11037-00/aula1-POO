#Remover espaços desnecessários entre palavras de um texto. def RemoverEspacos(texto)

def RemoverEspacos(texto):
 palavras = texto.split()
 resultado = ""
 for i in range (len(palavras)):
  resultado += palavras[i]
  if i != len(palavras) - 1:
   resultado += " "
 return resultado 
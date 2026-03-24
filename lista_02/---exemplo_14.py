#Obter o menor múltiplo comum (MMC) entre dois inteiros positivos x e y, utilizando a função MMC abaixo: def MMC(x, y)

def MMC(x, y):
 if x > y: maior = x
 else: maior = y 

 while True:
  if maior % x == 0 and maior % y == 0:
   return maior
  maior += 1

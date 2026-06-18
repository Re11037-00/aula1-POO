import enum

class Estacao(enum.Enum): 
    OUTONO = 1
    INVERNO =  2
    PRIMAVERA = 3
    VERAO = 4
a = Estacao.INVERNO
b = Estacao["OUTONO"]
c = Estacao(3)

print(a) # Estacao. INVERNO
print(b) #Estacao. VERAO
print(c) # Estacao. PRIMAVERA
print(c.name)
print(c.value)
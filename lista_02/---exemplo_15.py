#Verificar se um número é primo, utilizando a função Primo, abaixo: def Primo(n)

def Primo(n):
    primo = True
    for d in range(2,n):
        if n % d == 0: 
            primo = False
            break
    return primo

print("Digite um número inteiro")
n = int(input())

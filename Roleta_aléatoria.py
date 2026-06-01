from random import choice

print("======Roleta aléatoria de filmes======")


n = " "
resp = "Ss"
while resp not in "Nn":
    n = str(input("Digite o nome do filme: "))
    resp = str(input("Quer continuar? [S/N]: "))
    opcoes = [n]
sorteado = choice(opcoes)
print(sorteado)





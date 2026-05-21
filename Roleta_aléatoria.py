from random import choice

print("======Roleta aléatoria de filmes======")

n = 0

while n != " ":
    n = str(input("Digite o nome do filme: "))
    if n == " ":
        print("Digite o nome do filme")
        continue
    else:
        opcoes = [n]
        sorteado = choice(opcoes)
print("O escolhido foi {}".format(opcoes))








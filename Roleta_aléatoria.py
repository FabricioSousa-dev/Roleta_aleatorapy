import time
import random

totfilmes = 0
print("======Roleta aléatoria de filmes======")
for c in range(1,6):
    f1 = str(input("Digite o nome do {} filme: ".format(c)))
    totfilmes += 1
    opcoes = [f1]
    sorteador = random.choice(opcoes)


print("Tem {} filmes nessa roleta".format(totfilmes))

print("O filme selecionado foi {}".format(sorteador))





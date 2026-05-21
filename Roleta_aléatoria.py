import time
import random
print("======Roleta aléatoria de filmes======")
n = str
while n != 0 :
    n = str(input("Digite o nome do filme: "))
    opcoes = random.choice(n)
    if n == " ":
        print("Digite o nome do filme")
    else:
        opcoes = random.choice(n)

print("O escolhido foi {}".format(opcoes))








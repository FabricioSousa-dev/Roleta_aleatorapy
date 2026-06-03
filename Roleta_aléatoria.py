from random import choice

print("=="*30,end= "")
print("====Roleta aleatoria==================")

list = []
cont = 0
while True:
    cont += 1
    f = input(f"Digite o {cont} nome: ")
    opcao = str(input("Você quer continuar? [S/N]")).upper()
    list.append(f)
    while opcao not in "SN":
        print("Opcao invalida!", end="")
        opcao = str(input("Você quer continuar? [S/N]")).upper()
    if opcao == "N":
        break
sorteado = choice(list)
print(f"O escolhido foi {sorteado}")
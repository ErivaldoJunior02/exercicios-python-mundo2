print("======" "DESAFIO 68" "======")
from random import randint
print("Vamos jogar PAR ou ÍMPAR!")
vi = 0
while True:
    v = int(input("Digite um valor: "))
    j = str(input("Faça sua jogada [P/I]: ")).upper().split()[0]
    pc = randint(1, 10)
    s = v + pc
    p = s % 2
    if j in "Pp" and p == 0 or j in "Ii" and p == 1:
        print(("VOCÊ GANHOU! Vamos jogar mais uma vez!"))
        vi += 1
    if j in "Ii" and p == 0 or j in "Pp" and p == 1:
        if p == 0:
            print("DEU PAR!")
        if p == 1:
            print("DEU IMPAR!")
        break
print("Você jogou {} e o computador {}. Total de {}.".format(v, pc, v + pc))
print("GAME OVER. Você venceu {} vezes!".format(vi))

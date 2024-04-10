print("======" "DESAFIO 45" "======")
import random
import time
print("Vamos jogar um pedra, papel e tesoura!")
pc = ["PEDRA", "PAPEL", "TESOURA"]
e = random.choice(pc)
j = str(input("Faça sua jogada!: "))
je = j.upper()
print("VERIFICANDO...")
time.sleep(3)
if je == "PEDRA" and e == "PEDRA" or je == "PAPEL" and e == "PAPEL" or je == "TESOURA" and e == "TESOURA":
    print("EMPATE!")
elif je == "PEDRA" and e == "TESOURA" or je == "PAPEL" and e == "PEDRA" or je == "TESOURA" and e == "PAPEL":
    print("VOCÊ VENCEU!")
elif je == "PEDRA" and e == "PAPEL" or je == "PAPEL" and e == "TESOURA" or je == "TESOURA" and e == "PEDRA":
    print("VOCÊ PERDEU, TENTE DE NOVO!")
else:
    print("Favor escolher uma das opções entre PEDRA, PAPEL ou TESOURA!")
print("Eu escolhi {} e você escolheu {}!".format(e, je))
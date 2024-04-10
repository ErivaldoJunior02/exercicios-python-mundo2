print("======" "DESAFIO 58" "======")
import random
print("Pensei em um número entre 0 e 10.")
print("Você consegue adivinhar?")
t = 1
p = int(input("Que número eu pensei?: "))
pc = random.randint(0, 10)
while p != pc:
    if p > pc:
        print("Menos!")
    if p < pc:
        print("Mais")
    p = int(input("Você errou, tente denovo: "))
    t += 1
print("Parabéns, eu pensei em {} e você chutou {}, VOCÊ ACERTOU em {} tentativas!".format(p, pc, t))


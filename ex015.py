print("======" "DESAFIO 50" "======")
s = 0
co = 0
for c in range(1, 7):
    n = int(input("Digite o {}º número: ".format(c)))
    if n % 2 == 0:
        s += n
        co += 1
print("Você informou {} números pares e a soma foi {}".format(co, s))


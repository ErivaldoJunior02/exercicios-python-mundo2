print("======" "DESAFIO 53" "======")
f = str(input("Digite uma frase: ")).strip().upper()
p = f.split()
j = "".join(p)
i = ""
for l in range(len(j) - 1, -1, -1):
    i += j[l]
if i == j:
    print("O inverso de {} é {}".format(j, i))
    print("Temos um PALIDROMO")
else:
    print("O inverso de {} é {}".format(j, i))
    print("Não temos um PALIDROMO")
print("Você digitou a frase {}".format(f))


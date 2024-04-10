print("======" "DESAFIO 66" "======")
q = 0
s = 0
while True:
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break
    q += 1
    s += n
print("A quantidade de números informados foi {} e a soma entre eles é {}.".format(q, s))
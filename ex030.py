print("======" "DESAFIO 65" "======")
t = 0
c = "S"
qn = 0
ma = 0
me = 999
while c == "S":
    n = int(input("Digite um número: "))
    c = str(input("Quer continuar? [S/N] ")).upper().split()[0]
    t += 1
    qn += n
    if n > ma:
        ma = n
    if n < me:
        me = n
print("A média entre os {} termos que você apresentou é {}".format(t, qn / t))
print("O maior número informado foi {} e o menor foi {}".format(ma, me))

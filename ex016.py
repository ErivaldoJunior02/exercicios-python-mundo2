print("======" "DESAFIO 51" "======")
p = int(input("Primeiro termo: "))
r = int(input("Qual a razão?: "))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c)
print("======" "DESAFIO 60" "======")
from math import factorial
n = int(input("Digite um número: "))
c = n
f = factorial(n)
print("O fatorial de {}!".format(n))
while c > 0:
    print("{}".format(c), end = "")
    print(" x " if c > 1 else " = ", end = "")
    c -= 1
print("{}".format(f))
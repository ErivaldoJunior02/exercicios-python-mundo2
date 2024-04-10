print("======" "DESAFIO 64" "======")
s = 0
t = 0
n = 0
n = int(input("Digite um número [999 para parar]: "))
while n != 999:
    s += n
    t += 1
    n = int(input("Digite um número [999 para parar]: "))
print("A soma entre os {} termos que você digitou é {}".format(t, s))
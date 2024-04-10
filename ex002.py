print("======" "DESAFIO 37" "======")
n = int(input("Escolha um número inteiro qualquer: "))
e = int(input("Escolha para qual base de conversão 1 - binário, 2 - octal, 3 - hexadecimal: "))
if e == 1:
    print(bin(n))
elif e == 2:
    print(oct(n))
elif e == 3:
    print(hex(n))
else:
    print("Favor escolher uma das 3 opções informadas!")

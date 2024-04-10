print("======" "DESAFIO 59" "======")
p = float(input("Primeiro valor: "))
s = float(input("Segundo valor: "))
d = 0
while d != 5:
    print("=" * 20)
    print("O que deseja fazer?")
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")
    d = int(input("Qual sua opção?: "))
    print("=" * 20)
    if d == 1:
        print("A soma entre {} e {} é {}".format(p, s, p+s))
    elif d == 2:
        print("O produto entre {} e {} é {}".format(p, s, p*s))
    elif d == 3:
        if p > s:
            m = p
            print("O maior número entre {} e {} é {}".format(p, s, m))
        if s > p:
            m = s
            print("O maior número entre {} e {} é {}".format(p, s, m))
        if p == s:
            print("Não existe número maior!")
    elif d == 4:
        p = float(input("Digite um novo valor: "))
        s = float(input("Digite um novo segundo valor: "))
    elif d not in [1, 2, 3, 4, 5]:
        print("Opção inválida, tente novamente!")
print("Fim do programa!")

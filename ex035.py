print("======" "DESAFIO 70" "======")
print("=" * 20)
print("LISTA DE PRODUTOS")
print("=" * 20)
tg = 0
m100 = 0
while True:
    n = str(input("Nome do produto: "))
    p = float(input("Preço do produto: R$ "))
    tg += p
    if p >= 1000:
        m100 += 1
    c = str(input("Quer continuar [S/N]? "))
    if c in "Nn":
        break
print("O total gasto nessa lista é de R${}".format(tg))
print("{} produtos custaram mais de R$1.000,00".format(m100))


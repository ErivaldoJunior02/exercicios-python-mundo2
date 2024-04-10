print("======" "DESAFIO 69" "======")
print("=" * 20)
print("CADASTRO DE PESSOAS")
print("=" * 20)
p18 = 0
qh = 0
qm = 0
qm20 = 0
while True:
    i = int(input("IDADE: "))
    s = str(input("SEXO [F/M]: "))
    print("=" * 20)
    if i >= 18:
        p18 += 1
    if s in "Mm":
        qh += 1
    if s in "Ff" and i < 20:
        qm20 += 1
    c = str(input("Quer continuar [S/N]? "))
    print("=" * 20)
    if c in "Nn":
        break
print("No seu cadastro existem {} pessoas com mais de 18 anos.".format(p18))
print("No seu cadastro existem {} pessoas do sexo masculino.".format(qh))
print("No seu cadastro existem {} pessoas do sexo feminino com menos de 20 anos.".format(qm20))




print("======" "DESAFIO 56" "======")
si = 0
mv = 0
mih = 0
nv = ""
tm = 0
for c in range(1, 5):
    print("=" * 6, "{}º PESSOA".format(c), "=" * 6)
    n = str(input("Nome da {}º pessoa: ".format(c))).strip()
    i = int(input("Idade da {}º pessoa: ".format(c)))
    s = str(input("Sexo da {}º pessoa [M/F]: ".format(c))).upper().strip()
    si += i
    m = si / 4
    if c == 1 and s == "M":
        mih = i
        nv = n
    if s == "M" and i > mih:
        mih = i
        nv = n
    if s == "F" and i < 20:
        tm += 1
print("A média de idade do grupo é de {} anos!".format(m))
print("A idade do homem mais velho é de {} anos e seu nome é {}!".format(mih, nv))
print("Ao todo são {} mulheres com menos de 20 anos!".format(tm))
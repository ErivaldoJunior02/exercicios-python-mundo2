print("======" "DESAFIO 40" "======")
m1 = float(input("Qual sua nota?: "))
m2 = float(input("Qual a segunda nota?: "))
m = (m1 + m2) / 2
if m < 5:
    print("MÉDIA {:.2f}".format(m))
    print("REPROVADO!")
elif m > 5 and m < 6.9:
    print("MÉDIA {:.2f}".format(m))
    print("RECUPERAÇÃO!")
else:
    print("MÉDIA {:.2f}".format(m))
    print("APROVADO!")
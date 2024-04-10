print("======" "DESAFIO 41" "======")
from datetime import date
a = int(input("Ano de nascimento: "))
i = int(date.today().year) - a
print("A idade do atleta é {} anos!".format(i))
if i <= 9:
    print("Categoria MIRIM!")
elif i >= 10 and i <= 14 :
    print("Categoria INFANTIL!")
elif i >= 15 and i <= 19 :
    print("Categoria JUNIOR!")
elif i >= 20 and i <= 25:
    print("Categoria SÊNIOR!")
else:
    print("Categoria MASTER!")
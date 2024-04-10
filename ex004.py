print("======" "DESAFIO 39" "======")
from datetime import date
a = int(input("Qual o ano de seu nascimento?: "))
aa = date.today().year
i = aa - a
if i < 18:
    print("Ainda não é necessário se apresentar! Faltam {} anos.".format(18 - i))
elif i == 18:
    print("Você precisa se apresentar imediatamente!")
else:
    print("Você deveria ter se apresentado a {} anos!".format(i - 18))

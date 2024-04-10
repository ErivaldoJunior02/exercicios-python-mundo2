print("======" "DESAFIO 54" "======")
from datetime import date
atual = date.today().year
tm = 0
tme = 0
for c in range(1, 8):
    p = int(input("Em que ano a {}º pessoa nasceu?: ".format(c)))
    i = atual - p
    if i >= 21:
        tm += 1
    else:
        tme += 1
print("{} pessoas são maior de idade!".format(tm))
print("{} pessoas são menor de idade!".format(tme))

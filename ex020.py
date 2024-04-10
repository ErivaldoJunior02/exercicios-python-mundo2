print("======" "DESAFIO 55" "======")
ma = 0
me = 0
for c in range(1, 6):
    p = float(input("Qual o peso da {}º pessoa?: ".format(c)))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print("O maior peso lido foi {}Kg".format(ma))
print("O menor peso lido foi {}Kg".format(me))
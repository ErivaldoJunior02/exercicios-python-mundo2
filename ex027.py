print("======" "DESAFIO 62" "======")
t = int(input("Qual o primeiro termo?: "))
r = int(input("Qual a razão PA?: "))
d = 10
qt = 0
while d > 0:
    print(t, end = " -> ")
    t += r
    d -= 1
    qt +=1
    if d == 0:
        o = int(input("Quantos termos você quer mostrar a mais?: "))
        d = o
        if o == 0:
            print("Fim do programa, com {} termos!".format(qt))

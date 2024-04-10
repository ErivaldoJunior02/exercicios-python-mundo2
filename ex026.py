print("======" "DESAFIO 61" "======")
t = int(input("Qual o primeiro termo?: "))
r = int(input("Qual a razão PA?: "))
d = 9
while d > 0:
    print(t, end = " -> ")
    t += r
    d -= 1
print(t)
print("FIM")
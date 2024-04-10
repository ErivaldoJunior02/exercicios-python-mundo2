print("======" "DESAFIO 42" "======")
p = float(input("Digite o tamanho de uma reta: "))
s = float(input("Digite o tamanho de outra reta: "))
t = float(input("Digite o tamanho de mais uma reta: "))
if p < s + t and s < p + t and t < p + s:
    print("Essas retas podem formar um TRIÂNGULO!")
    if p == s and p == t:
        print("É um triãngulo EQUILÁTERO!")
    elif p == s and p / t or p == t and p / s or s == t and s / p:
        print("É um triângulo ISÓSCELES!")
    elif p / s and p / t or s / p and s / t or t / p and t / s:
        print("É um triângulo ESCALENO!")
else:
    print("Essas retas NÃO podem formar um TRIÂNGULO!")
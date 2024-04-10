print("======" "DESAFIO 44" "======")
v = float(input("Qual o valor do produto?: R$"))
print("Formas de pagamento: 1 - Á vista, 2 - Á vista no cartão, 3 - 2x no cartão, 4 - Mais de 3x no cartão")
f = int(input("Qual a forma de pagamento?: "))
if f == 1:
    print("O total a pagar será de R${}, com um desconto de 10%!".format(v - v * 10/100))
elif f == 2:
    print("O total a pagar será de R${}, com um desconto de 5%!".format(v - v * 5/100))
elif f == 3:
    print("O total a pagar sera de R${}, sem juros!".format(v))
elif f == 4:
    print("O total a pagar será de R${}, com 20% de juros!".format(v + v * 20/100))
else:
    print("Favor escolher uma das opções acima!")
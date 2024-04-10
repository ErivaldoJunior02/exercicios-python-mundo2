print("======" "DESAFIO 36" "======")
vc = float(input("Qual o valor da casa?: R$"))
s = float(input("Qual o seu salário?: R$"))
a = int(input("Em quantos anos pretende pagar?: "))
p = a * 12
pm = vc / p
m = 30/100 * s
if pm <= m:
    print("Seu empréstimo foi aprovado com R${:.2f} por mês!".format(pm))
else:
    print("A parcela de R${:.2f} ao exeder 30% do seu salário que equivale a R${:.2f}, seu empréstimo foi negado!".format(pm, m))
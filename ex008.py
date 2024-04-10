print("======" "DESAFIO 43" "======")
p = float(input("Qual seu peso em Kg?: "))
a = float(input("Qual sua altura em metros?: "))
imc = p / a**2
if imc < 18.5:
    print("Seu IMC é de {:.2f}, voçê está ABAIXO do peso!".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu IMC é de {:.2f}, você está no peso IDEIAL!".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu IMC é de {:.2f}, você está com SOBREPESO!".format(imc))
elif imc >= 30 and imc < 40:
    print("Seu IMC é de {:.2f}, você está com OBESIDADE!".format(imc))
else:
    print("Seu IMC é de {:.2f}, você está com OBESIDADE MÓRBIDA!".format(imc))
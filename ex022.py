print("======" "DESAFIO 57" "======")
sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dado inválido, por favor informe seu sexo: ")).strip().upper()[0]
print("Você é do sexo {}".format(sexo))
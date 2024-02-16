n1 = float(input("Nota um: "))
n2 = float(input("Nota segunda: "))
media = float((n1+n2)/2)
print("Sua média é: ", media)

if media >= 7:
    print("você foi aprovado.")
elif media == 10:
    print("Você foi aprovado com distinção.")
else:
    print("Você foi reprovado.")
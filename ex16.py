valor=int(input("Digite um valor "))
if valor >=0 and valor<=10:
    print("Está entre 0 e 10")
elif valor >=11 and valor <=20:
    print("Está entre 11 e 20")
elif valor >=21 and valor <=30:
    print("Está entre 21 e 30")
elif valor >30:
    print("É maior que 30")
else:
    print("Valor negativo")
print(f"O valor digitado foi {valor}")
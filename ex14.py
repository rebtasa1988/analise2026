"""idade = int(input("Digite o sua idade "))
gênero = str(input("Digite o seu gênero "))
if (idade>=18) and (gênero == "masculino"):
    print (f"Você tem {idade} anos, e é do gênero {gênero}, foi aprovado para o alistamento!")
else:
    print(f"Você tem {idade} anos, você não foi aprovado para o alistamento!")"""

gênero = input("Digite m-masculino e f-feminino ").upper()
idade=int(input("Digite a idade "))
if gênero == "M" and idade>=18:
    print("Apto a se alistar")
else:
    print("Inapto a se alistar")
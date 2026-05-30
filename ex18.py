#Descrição de Cargo
cargo = input("Digite o cargo do colaborador ")

if cargo == "caixa" :
    sal = 1500
elif cargo == "vendedor" :
    sal = 2400
elif cargo == "gerente" :
        sal = 4000
else:
    sal = 0
    print("Cargo não existe!")
inss = sal *0.12
if (sal>200):
     irrf = sal*0.14
else:
     irrf = sal*0.08
salfinal = sal - irrf - inss
print(f"seu salário é {sal}")
print(f"o inss é {inss}")
print(f"o irrf é {irrf}")
print(f"o salário final é {salfinal}")
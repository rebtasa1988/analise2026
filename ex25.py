"""x=int(input("digite um valor"))
valor=x%2
print(valor)"""

n=0
for i in range (0,5):
    x=int(input("digite um valor "))
    v=x%2
    if v == 1:
        print(f"o valor {x} é impar")
    else:
        print(f"o valor {x} é par")
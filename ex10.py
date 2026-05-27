anon=int(input("Digite seu ano de nascimento "))
anoa=int(input("Digite o ano atual "))
idade=anoa-anon
if idade>= 18:
    print(f"Você tem {idade} anos. Parabéns você é maior de idade!")
else:
    print(f"Você tem {idade} anos. Atenção, você é menor de idade!")

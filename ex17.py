dia = (input("Digite o dia da semana "))
Hora = int(input("Informe que horas a aula finalizou "))

if dia == "sexta" and Hora == 21:
    print("Sextou! Você merece 1 chopp")
elif dia == "sexta" and Hora == 22:
    print("Sextou! Você merece pelo menos 2 chopps")
else:
    print("Ainda não sextou! Não saia da rotina, e vá estudar!")
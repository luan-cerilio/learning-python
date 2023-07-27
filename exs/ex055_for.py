for i in range(1, 6):
    peso = float(input('Informe seu peso (kg): '))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso é {maior:.1f} (kg) e o menor {menor:.1f} (kg).')
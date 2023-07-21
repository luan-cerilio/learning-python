peso = float(input('Peso (kg): '))
alt = float(input('Altura (m): '))
imc = peso / (alt * alt)
print(f'Seu imc: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
frase = str(input('Insira a frase: ')).strip().lower().replace(' ', '')
if frase == frase[::-1]:
    print('Palíndromo.')
else:
    print('Não é um palíndromo.')
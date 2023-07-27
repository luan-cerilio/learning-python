from datetime import date
count = 0
for i in range(1, 8):
    idade = date.today().year - int(input('Informe seu ano de nascimento: '))
    print(f'Sua idade: {idade}')
    if idade > 20:
        count += 1
print(f'{count} pessoas já atingiram a maioridade.')
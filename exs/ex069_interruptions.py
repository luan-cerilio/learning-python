idade = count18 = countH = countM = 0
sexo = nome = continuar = ''
print('Cadastro de pessoas.')
while True:
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo: [m/f] ')).strip().lower()
    idade = int(input('Idade: '))
    if idade > 18:
        count18 += 1
    if sexo in 'm':
        countH += 1
    if sexo in 'f' and idade < 20:
        countM += 1
    continuar = str(input('Deseja cadastrar mais uma pessoa? [s/n] ')).strip().lower()
    if continuar in 'n':
        break
print(f'Pessoas com mais de 18 anos: {count18}')
print(f'Homens: {countH}')
print(f'Mulheres com menos de 20 anos: {countM}')

nome = []
idade = []
sexo = []
soma = 0
velho = 0
first = True
mulheres = 0
for i in range(0, 4):
    nome.append(str(input('Informe seu nome: ')))
    idade.append(int(input('Informe sua idade: ')))
    soma = soma + idade[i]
    sexo.append(int(input('Informe seu sexo: \n[ 1 ] MASC\n[ 2 ] FEM\n')))
    if sexo[i] == 1:
        if first == True:
            first = False
            velho = i
        elif idade[i] > idade[velho]:
            velho = i
    elif sexo[i] == 2:
        if idade[i] < 20:
            mulheres = mulheres + 1
    else:
        print('OPÇÃO INVÁLIDA!!!')
print(f'Média de idade do grupo: {soma/4}')
print(f'O homem mais velho é o {nome[velho]}, com {idade[velho]} anos.')
print(f'Há {mulheres} mulheres com menos de 20 anos.')
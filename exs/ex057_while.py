s = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while s not in 'MF':
    print('Opcao Invalida!!')
    s = str(input('Informe seu sexo: [M/F] ')).strip().upper()
print('Registrado com sucesso!')
        
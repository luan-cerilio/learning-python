n1 = float(input('n1 = '))
n2 = float(input('n2 = '))
sair = False
while not sair:
    op = int(input('''Selecione:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa
'''))
    if op == 1:
        print(f'n1 + n2 = {n1 + n2:.2f}')
    elif op == 2:
        print(f'n1 x n2 = {n1 * n2:.2f}')
    elif op == 3:
        print(f'n1 = {n1:.2f}' if n1 > n2 else f'n2 = {n2:.2f}')
    elif op == 4:
        n1 = float(input('n1 = '))
        n2 = float(input('n2 = '))
    elif op == 5:
        sair = True
        print('Tchau!')
    else:
        print('Opcao invalida!!! Tente novamente\n')
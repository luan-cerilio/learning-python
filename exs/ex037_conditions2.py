num = int(input('Entre com um inteiro qualquer: '))
base = int(input('Qual será a base de conversão?\n1 - binário\n2 - octal\n3 - hexadecimal\n'))

if base == 1:
    print(f'Binário: {bin(num)}')
elif base == 2:
    print(f'Octal: {oct(num)}')
elif base == 3:
    print(f'Hexadecimal: {hex(num)}')
else:
    print('\033[4;30;41mBase informada não disponível!\033[m')
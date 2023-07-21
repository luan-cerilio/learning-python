n1 = int(input('n1: '))
n2 = int(input('n2: '))

if n1 > n2:
    print('O \033[4;30;41mprimeiro\033[m valor é maior.')
elif n1 < n2:
    print('O \033[4;30;41msegundo\033[m valor é maior.')
else:
    print('Não existe valor maior, os dois são \033[4;30;41miguais\033[m.')

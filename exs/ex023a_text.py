num = int(input('Digite um número (0 a 9999): '))
uni = str(num)[0]
if num > 9:
    dez = str(num)[1]
else:
    dez = 0
if num > 99:
    cen = str(num)[2]
else:
    cen = 0
if num > 999:
    mil = str(num)[3]
else:
    mil = 0
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(uni, dez, cen, mil))
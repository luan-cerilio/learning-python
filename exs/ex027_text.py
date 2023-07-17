name = str(input('Digite seu nome completo: '))
name = name.split()
first = name[0]
last = name[len(name)-1]
print('Seu primeiro nome é: {}'.format(first))
print('Seu último nome é: {}'.format(last))
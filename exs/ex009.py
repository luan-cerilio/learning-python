n = int(input('Digite um numero para obter sua tabuada: '))
i = 1
print('-' * 10)
for i in range(11):
    print('{} x {:2} = {}'.format(n, i, i*n))
print('-' * 10)
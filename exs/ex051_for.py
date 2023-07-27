print('### Progressão Aritmética ###')
print('an = a1 + (n - 1) * r')
a1 = int(input('Primeiro termo (a1): '))
r = int(input('Razão (r): '))
for n in range (1, 11):
    print(f'{a1 + (n - 1) * r}', end = ' ')

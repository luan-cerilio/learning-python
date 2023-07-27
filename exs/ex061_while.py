print('### Progressão Aritmética ###')
print('an = a1 + (n - 1) * r')
a1 = int(input('Primeiro termo (a1): '))
r = int(input('Razão (r): '))
n = 1
while n <= 10:
    print(f'{a1 + (n - 1) * r}', end = ' ')
    n += 1
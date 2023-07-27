print('### Progressão Aritmética ###')
print('an = a1 + (n - 1) * r')
a1 = int(input('Primeiro termo (a1): '))
r = int(input('Razão (r): '))
termos = 10
while termos > 0:
    for n in range(1, termos+1):
        print(f'{a1 + (n - 1) * r}', end = ' ')
    a1 = a1 + n * r
    termos = int(input('\nVoce quer mostrar mais termos? Digite a quantidade: '))
    print('Tchau!' if termos <= 0 else '', end = '')

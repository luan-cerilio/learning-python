count = int(input('Fibonnaci. Quantos termos após 0, 1? '))
n0 = 0
n1 = 1
while count > 0: 
    count -= 1
    if n0 == 0 and n1 == 1:
        print(f'0 → 1 ', end = '→ ')
        n2 = 0
    n2 = n1 + n0
    n0 = n1
    n1 = n2
    print(f'{n2} → ' if count > 0 else f'{n2}', end = '')

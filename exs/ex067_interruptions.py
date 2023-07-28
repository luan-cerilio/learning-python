n = 0
print('Tabuada')
while True:
    n = int(input('n = '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')

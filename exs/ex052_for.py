n = int(input('n = '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print('Primo' if count == 2 else 'Nao eh primo')
sum = 0
for i in range (1, 7):
    n = int(input(f'n{i}: '))
    if n % 2 == 0:
        sum += n
print(sum)
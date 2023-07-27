## Soma de todos impares multiplos de 3 entre 1 e 500
sum = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        sum += i
print(sum)
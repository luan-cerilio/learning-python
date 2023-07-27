n = int(input('n = '))
fat = 1
while n != 0:
    fat = fat * n
    n = n - 1
print(f'Fatorial = {fat}')
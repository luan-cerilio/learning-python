n = s = c = 0
while True:
    n = int(input('n = '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Soma: {s}')
print(f'Count: {c}')

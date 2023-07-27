n = soma = count = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        soma += n
        count += 1
print(f'Foram digitados {count} numeros. A soma das entradas eh {soma}')
    
flag = 's'
maior = soma = count = 0
while flag in 's':
    n = int(input('Digite um inteiro: '))
    count += 1
    if count == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    flag = str(input('Deseja continuar? [s/n] ')).strip().lower()
print(f'Maior = {maior}\nMenor = {menor}\nMedia = {soma/count:.2f}')
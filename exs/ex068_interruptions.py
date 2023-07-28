from random import randint
count = pc = 0
userChoice = ''
userNumber = 0
while True:
    pc = randint(0, 10)
    userChoice = str(input('Par ou ímpar? [p/i] ')).strip().lower()
    userNumber = int(input('Informe seu número: '))
    sum = pc+userNumber
    if userChoice in 'p' and sum % 2 == 0:
        print(f'Você venceu! Número jogado pelo pc: {pc}. Total {sum} (par).')
        count += 1
    elif userChoice in 'i' and sum % 2 != 0:
        print(f'Você venceu! Número jogado pelo pc: {pc}. Total {sum} (ímpar).')
        count += 1
    else:
        print(f'Você perdeu! :( Número jogado pelo pc: {pc}. Total {sum} ', end ='')
        print('(par).' if sum % 2 == 0 else '(ímpar).')
        print(f'Total de vitórias consecutivas: {count}')
        break

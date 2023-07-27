from random import randint
acertou = False
tentativas = 0
while not acertou:
    tentativas += 1
    numPC = randint(0, 10)
    numUser = int(input('Adivinhe o número sorteado pelo PC! '))
    if numUser == numPC:
        print('Acertou! :DDDD')
        print(f'tentativas: {tentativas}')
        acertou = True
    else:
        print('EROOOOU')
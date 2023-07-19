import random
numPC = random.randint(0, 5)
numUser = int(input('Adivinhe o número sorteado pelo PC! '))
if numUser == numPC:
    print('Acertou! :DDDD')
else:
    print('EROOOOU')
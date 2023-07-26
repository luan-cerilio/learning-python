from random import randint
from time import sleep

# WELCOME PROMPT
print(f'''BEM-VINDO(A) AO JOKENPÔ!

Para jogar, selecione uma das opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA\n''')

user = int(input('Qual a sua escolha? '))

# MACHINE MOVES
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!\n')
sleep(1)

mac = randint(1, 3)
print('-='*13)
if mac == 1:
    print('A máquina selecionou PEDRA')
elif mac == 2:
    print('A máquina selecionou PAPEL')
else:
    print('A máquina selecionou TESOURA')
print('-='*13)

print('\n')
# WHO WON
if user == mac:
    print('EMPATE')
elif user == 1 and mac == 2:
    print('A MÁQUINA VENCEU! Pedra perde de Papel.')
elif user == 1 and mac == 3:
    print('VOCÊ VENCEU! Pedra ganha de Tesoura.')
elif user == 2 and mac == 1:
    print('VOCÊ VENCEU! Papel ganha de Pedra.')
elif user == 2 and mac == 3:
    print('A MÁQUINA VENCEU! Papel perde de Tesoura.')
elif user == 3 and mac == 1:
    print('A MÁQUINA VENCEU! Tesoura perde de Pedra.')
elif user == 3 and mac == 2:
    print('VOCÊ VENCEU! Tesoura ganha de Papel.')

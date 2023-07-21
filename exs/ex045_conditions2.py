from random import choice
from time import sleep

# WELCOME PROMPT
print(f'\033[4;30;41mBEM-VINDO(A) AO JOKENPÔ!\033[m')
print(f'Para jogar, selecione uma das opções:')
user = int(input(f'1 Pedra ✊🏽\n2 Papel ✋🏽\n3 Tesoura ✌🏽\n'))

# MACHINE MOVES
op = [1, 2, 3]
print(f'A máquina está escolhendo seu movimento...')
sleep(3)
mac = choice(op)
if mac == 1:
    print('A máquina selecionou Pedra ✊🏽')
elif mac == 2:
    print('A máquina selecionou Papel ✋🏽')
else:
    print('A máquina selecionou Tesoura ✌🏽')

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

print(f'\033[4;30;41mFIM DO JOGO!\033[m')    
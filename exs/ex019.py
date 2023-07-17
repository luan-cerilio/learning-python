from random import choice
aluno1 = input('Aluno1: ')
aluno2 = input('Aluno2: ')
aluno3 = input('Aluno3: ')
aluno4 = input('Aluno4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
selec = choice(lista)
print('O aluno escolhido é o Aluno{}: {}'.format(lista.index(selec)+1, selec))
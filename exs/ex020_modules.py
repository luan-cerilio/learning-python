import random
aluno1 = input('Aluno1: ')
aluno2 = input('Aluno2: ')
aluno3 = input('Aluno3: ')
aluno4 = input('Aluno4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de apresentação é:\n1 - {}\n2 - {}\n3 - {}\n4 - {}'.format(lista[0], lista[1], lista[2], lista[3]))
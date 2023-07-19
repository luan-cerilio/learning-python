name = str(input('Digite o seu nome: '))
silva = 'silva' in name.lower().split()
print('Não possui Silva.' if silva == False else 'Possui Silva!')
name = str(input('Digite o seu nome: '))
silva = name.lower().find('silva')
print('Não possui Silva.' if silva == -1 else 'Possui Silva!')
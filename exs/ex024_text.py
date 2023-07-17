cid = str(input('Digite o nome da sua cidade: '))
santo = cid.split()[0].lower().find('santo')
if santo != -1:
    print('Começa com Santo!')
else:
    print('Não começa com Santo.')
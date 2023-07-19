dist = float(input('Qual a distância da sua viagem? (km) '))
if dist > 200.0:
    print(f'> 200 km. Sua passagem irá custar R$ {dist*0.45:.2f}')
else:
    print('<= 200 km. Sua passagem irá custar R$ {:.2f}'.format(dist*0.50))
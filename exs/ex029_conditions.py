vel = int(input('Velocidade (km/h): '))
if vel > 80:
    print('Você foi multado! Valor da multa: R$ {}'.format(7*(vel-80)))
else:
    print('Dentro do limite de velocidade permitido.')
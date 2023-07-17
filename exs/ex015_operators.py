dias = int(input('Quantos dias vc usou o carro? '))
km = float(input('Quantos km vc rodou? '))
pagar = dias * 60 + 0.15 * km
print('Vc ira pagar R$ {:.2f} no total'.format(pagar))
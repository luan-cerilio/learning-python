from math import sqrt
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = sqrt(co*co+ca*ca)
print('A hipotenusa é: {:.2f}'.format(hip))
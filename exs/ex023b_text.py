num = int(input('Digite um número (0 a 9999): '))
uni = num%10
dez = (num//10)%10
cen = (num//100)%10
mil = (num//1000)%10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(uni, dez, cen, mil))
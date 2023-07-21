n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
avg = (n1 + n2) / 2
if avg < 5.0:
    print('REPROVADO')
elif avg < 6.9:
    print('RECUPERAÇÃO')
else: 
    print('APROVADO')
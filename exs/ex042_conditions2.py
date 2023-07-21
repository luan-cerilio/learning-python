A = int(input('Lado A do triângulo: '))
B = int(input('Lado B do triângulo: '))
C = int(input('Lado C do triângulo: '))

if A + B > C and B + C > A and A + C > B:
    print('É possível formar um triângulo!')
    if A == B and B == C:
        print('EQUILÁTERO')
    elif A == B or B == C or C == A:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não é possível formar um triângulo!')
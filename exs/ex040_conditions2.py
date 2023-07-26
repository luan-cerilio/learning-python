n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
avg = (n1 + n2) / 2
if avg < 5.0:
    print(f'REPROVADO ({avg:.1f})')
elif avg < 7:
    print(f'RECUPERAÇÃO ({avg:.1f})')
else: 
    print(f'APROVADO ({avg:.1f})')
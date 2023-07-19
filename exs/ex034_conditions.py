sal = float(input('Informe seu salário: R$ '))
if sal > 1250.00:
    print(f'Seu aumento é de R$ {sal*0.1:.2f}. Novo salário: R$ {sal*1.1:.2f}')
else:
    print(f'Seu aumento é de R$ {sal*0.15:.2f}. Novo salário: R$ {sal*1.15:.2f}')
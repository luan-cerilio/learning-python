valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Seu salário: R$ '))
anos = int(input('Em quantos anos você vai pagar? '))

prestacao = valorCasa / (anos * 12)

if prestacao > salario*0.3:
    print(f'Empréstimo \033[4;30;41mNEGADO\033[m!\nPrestação: R$ {prestacao:.2f} > 30% de R$ {salario:.2f} (R$ {salario*0.3:.2f})')
else:
    print(f'Emprestimo \033[4;30;42mCONCEDIDO\033[m!\nPrestação: R$ {prestacao:.2f} < 30% de R$ {salario:.2f} (R$ {salario*0.3:.2f})')
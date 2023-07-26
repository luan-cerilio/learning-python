price = float(input('Preço da compra: R$ '))
cond = int(input('''Condições de pagamento:
[ 1 ] À vista dinheiro/pix (10% desconto)
[ 2 ] À vista cartão (5% desconto)
[ 3 ] 2x cartão (sem desconto)
[ 4 ] 3x ou mais cartão (20% de juros)
Qual a opção? '''))
if cond == 1:
    print(f'Op 1 selecionada.\nNovo preço (10% desconto): R$ {price*0.90:.2f}')
elif cond == 2:
    print(f'Op 2 selecionada.\nNovo preço (5% desconto): R$ {price*0.95:.2f}')
elif cond == 3:
    print(f'Op 3 selecionada.\n2 parcelas de R$ {price/2:.2f}\nValor total: R$ {price:.2f}')
elif cond == 4:
    print('Op 4 selecionada.')
    parc = int(input('Quantas parcelas? '))
    if parc > 2:
        print(f'{parc} parcelas de R$ {price*1.2/parc:.2f}\nValor total (Juros 20%): R$ {price*1.2:.2f}')
    else:
        print('Valor de parcelas inválido para essa opção. Selecione 3 ou mais!')
else:
    print('\033[4;30;41mCondição não existente!\033[m')
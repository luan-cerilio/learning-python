price = float(input('Preço produto: R$ '))
cond = int(input('Condição de pagamento:\n1 - À vista dinheiro/pix (10% desconto)\n2 - À vista cartão (5% desconto)\n3 - 2x cartão (sem desconto)\n4 - 3x ou mais cartão (20% de juros)\n'))
if cond == 1:
    print(f'Op 1 selecionada.\nNovo preço (10% desconto): R$ {price*0.90:.2f}')
elif cond == 2:
    print(f'Op 2 selecionada.\nNovo preço (5% desconto): R$ {price*0.95:.2f}')
elif cond == 3:
    print(f'Op 3 selecionada.\nPreço se mantém: R$ {price:.2f}')
elif cond == 4:
    print(f'Op 4 selecionada.\nNovo preço (Juros 20%): R$ {price*1.2:.2f}')
else:
    print('\033[4;30;41mCondição não existente!\033[m')
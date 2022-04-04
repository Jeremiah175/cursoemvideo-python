print('{:=^40}'.format('LOJAS TABAJARA'))
preço = float(input('Qual o valor total das compras: R$ '))
print('''FORMA DE PAGAMENTO:
[ 1 ] à vista em DINHEIRO/CHEQUE
[ 2 ] à vista no CARTÃO
[ 3 ] 2x no CARTÃO
[ 4 ] 3x ou mais no CARTÃO''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * (10/100))
elif opção == 2 :
    total = preço - (preço * (5/100))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * (20/100))
    totparcelas = int(input('Quantas vezes que parcelas? '))
    parcela = total / totparcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparcelas, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDADE de pagamento, tente novamente')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final!'.format(preço, total))

valor_pago = float(input('Valor pago: '))
valor_investido = float(input('Valor investido: '))
valor_venda = float(input('Valor da venda: '))

custo_total = valor_pago + valor_investido
lucro = valor_venda - custo_total

if lucro > 0:
    print(f'A venda teve um lucro de: {lucro}')
elif lucro < 0:
    print(f'A venda teve um prejuízo de: {lucro}')
else:
    print('A venda não teve lucro nem prejuízo')

temp = int(input('Qual é a temperatura: ' ))
if temp < 0:
    print('Congelando.....')

elif 0 <= temp <= 20:
    print('frio...')

elif 21 <= temp <= 25:
    print('Normal')

elif 26 <= temp <= 35:
    print('Quente')
else:
    print('Muito quente!')
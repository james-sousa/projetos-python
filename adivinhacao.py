print('***************************')
print('***jogo da adivinhação***')
print('***************************')

numero_secreto = 23
chute = input('Digite o seu número: ')
print('Você digitou: ', chute)

if(numero_secreto == chute):
    print('Você acertou')

else:
    print('Você errou')
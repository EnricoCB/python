from random import choice
import emoji
lista  = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)
user = str(input('Escolha pedra, papel ou tesoura: ')).capitalize()
if user == 'Papel' or user == 'Tesoura' or user == 'Pedra':
    print('-'*30)
    print (f"""Você escolheu {user}
    O computador escolheu {computador}""")
    print('-'*30)
    if user == 'Papel' and computador == 'Tesoura':
        print(emoji.emojize(':hand:', use_aliases=True))
        print(emoji.emojize(':v:', use_aliases=True))
        print('O COMPUTADOR GANHOU')
    elif user == 'Papel' and computador == 'Papel':
        print(emoji.emojize(':hand:', use_aliases=True))
        print(emoji.emojize(':hand:', use_aliases=True))
        print('EMPATE')
    elif user == 'Papel' and computador == 'Pedra':
        print(emoji.emojize(':hand:', use_aliases=True))
        print(emoji.emojize(':fist:', use_aliases=True))
        print('VOCÊ GANHOU')
    elif user == 'Tesoura' and computador == 'Tesoura':
        print(emoji.emojize(':v:', use_aliases=True))
        print(emoji.emojize(':v:', use_aliases=True))
        print('EMPATE')
    elif user == 'Tesoura' and computador == 'Papel':
        print(emoji.emojize(':v:', use_aliases=True))
        print(emoji.emojize(':hand:', use_aliases=True))
        print('VOCÊ GANHOU')
    elif user == 'Tesoura' and computador == 'Pedra':
        print(emoji.emojize(':v:', use_aliases=True))
        print(emoji.emojize(':fist:', use_aliases=True))
        print('O COMPUTADOR GANHOU')
    elif user == 'Pedra' and computador == 'Tesoura':
        print(emoji.emojize(':fist:', use_aliases=True))
        print(emoji.emojize(':v:', use_aliases=True))
        print('VOCÊ GANHOU')
    elif user == 'Pedra' and computador == 'Papel':
        print(emoji.emojize(':fist:', use_aliases=True))
        print(emoji.emojize(':hand:', use_aliases=True))
        print('O COMPUTADOR GANHOU')
    elif user == 'Pedra' and computador == 'Pedra':
        print(emoji.emojize(':fist:', use_aliases=True))
        print(emoji.emojize(':fist:', use_aliases=True))
        print('EMPATE')
else:
    print('Jogada invalida')

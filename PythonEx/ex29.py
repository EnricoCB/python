velocidade = int(input('A que velocidade o carro estava? '))
if velocidade > 80:
    m = (velocidade - 80) * 7
    print(f'Você foi multado em {m}, por estar acima do limite de velocidade')

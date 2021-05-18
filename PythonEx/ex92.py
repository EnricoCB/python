from datetime import date
ano = date.today().year
c = 0
dados = dict()
dados['nome'] = input('Nome: ')
dados['idade'] = int(input('Data de nascimento: '))
dados['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['carteira'] != 0:
    c = 1
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] - dados['idade']) + 35
dados['idade'] = ano - dados['idade']
print(f'Nome: {dados["nome"]}')
print(f'Idade: {dados["idade"]}')
print(f'Ctps: {dados["carteira"]}')
if c == 1:
    print(f'Contratação: {dados["contratação"]}')
    print(f'Salário: {dados["salário"]}')
    print(f'Aposentadoria: {dados["aposentadoria"]}')

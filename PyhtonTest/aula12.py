nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print('seu nome é bem comum no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')
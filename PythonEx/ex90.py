aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['Média'] = int(input(f'A Média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["Média"]}')
print(f'Situação: {aluno["situação"]}')
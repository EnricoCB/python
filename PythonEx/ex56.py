
for c in range (1,5):
    sexo = str(input('Digite [M] para masculino e [F] para feminino: '))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    if c == 1:
        maiornome = ''
        média = 0
        contador = 0
        maior = 0
        maior = idade
    else:
        if sexo == 'M' and idade > maior:
            maiornome = nome[0:]
        if sexo == 'F' and idade < 20:
            contador += 1
    média += idade
média = média/c
print(f'A média de idade desse grupo é {média}\nO nome do homem mais velho é {maiornome}\n{contador} Mulheres tem menos que 20 anos')
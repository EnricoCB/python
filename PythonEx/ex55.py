peso = float(input('Digite o seu peso: '))
maior = peso
menor = peso
for c in range (1,5):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'{maior}KG foi o maior peso\n{menor}KG foi o menor peso')

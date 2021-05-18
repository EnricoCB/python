ne = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número de 0 a 20: '))
while True:
    if n <= 20 and n > 0:
        break
    else:
        n = int(input('Tente novamente. Digite um número de 0 a 20: '))

for cont in range (0, len(ne)):
    if cont == n:
        print(f'O número por extenso é {ne[cont]}') 

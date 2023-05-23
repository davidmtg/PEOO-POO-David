n1 = int(input('Digite a nota do primeiro bimestre da disciplina: '))
n2 = int(input('Digite a nota do segundo bimestre da disciplina: '))

media = ((n1 * 2) + (n2 * 3)) / (2 + 3)

if int(media) == media:
    media = int(media)
    
print(f'Média parcial = {media}')
base = int(input('Digite a base do retângulo:'))
altura = int(input('Digite a altura do retângulo:'))

area = base * altura
perimetro = base * 2 + altura * 2
diagonal = (base**2 + altura**2) ** (1/2)

print(f'Área = {area:.2f}, Perímetro = {perimetro:.2f}, Diagonal = {diagonal:.2f}')
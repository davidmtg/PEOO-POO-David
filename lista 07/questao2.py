x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))
def maior(x, y, z):
  maior = x
  if y > maior:
    maior = y
  if z > maior:
    maior = z
  return maior

print(f'Maior número: {maior(x, y, z)}')
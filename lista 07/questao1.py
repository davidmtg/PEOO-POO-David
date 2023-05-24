x = int(input('Digite um número: '))
y = int(input('Digite um número: '))

def maior(x, y):
  maior = x
  if y > maior:
    maior = y
  return maior

print(f'Maior número: {maior(x, y)}')
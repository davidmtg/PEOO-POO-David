print('Digite dois valores inteiros separados por um sinal')
operacao = input()
if '+' in operacao:
  a, b = map(int, operacao.split('+'))
  calc = a + b
elif '-' in operacao:
  a, b = map(int, operacao.split('-')) 
  calc = a - b
elif '*' in operacao:
  a, b = map(int, operacao.split('*'))
  calc = a * b
elif '/' in operacao:
  a, b = map(int, operacao.split('/'))
  calc = a / b
print(f'O resutado da operação é {calc}')  
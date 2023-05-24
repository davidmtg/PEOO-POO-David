n1 = int(input('Digita sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))

def aprovado(n1, n2):
  media = (n1+n2)/2
  situacao = ''
  if media >= 60:
    situacao = print('Aprovado')
  else:
    situacao = print('Prova final')

print(f'Situação: {aprovado(n1, n2)}')
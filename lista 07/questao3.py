nome_completo = input('Digite o seu nome completo: ')

def iniciais(nome_completo):
  palavras = nome_completo.split()
  iniciais = ''
  for palavra in palavras:
    iniciais += palavra[0]
  return iniciais

print(f'Iniciais do nome: {iniciais(nome_completo)}')
  
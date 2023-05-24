entrada = int(input())
total = ratos = coelhos = sapos = 0

for i in range(entrada):
    quantia, tipo = input().split()
    quantia = int(quantia)
    total += quantia
    if tipo == 'C':
        coelhos += quantia
    if tipo == 'R':
        ratos += quantia
    if tipo == 'S':
        sapos += quantia
    
    coelhosporcentagem = (100 * coelhos) / total 
    ratosporcentagem = (100 * ratos) / total 
    saposporcentagem = (100 * sapos) / total 
        
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {coelhosporcentagem:.2f} %')
print(f'Percentual de ratos: {ratosporcentagem:.2f} %')
print(f'Percentual de sapos: {saposporcentagem:.2f} %')



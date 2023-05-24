n = int(input())
x=0

for i in range(1,100):
    y = int(input())
    if y > x:
        maior = y
        posicao = i + 1
        x = y

print(maior)
print(posicao)




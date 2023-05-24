n = list(map(int, input().split()))
n.sort()
a, b = n
if b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
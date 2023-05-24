a1 = int(input())
a2 = int(input())
a3 = int(input())

a1_min = a2 * 2 + a3 * 4
a2_min = a1 * 2 + a3 * 2
a3_min = a1 * 4 + a2 * 2
    
lista_min = [a1_min, a2_min, a3_min]
lista_min.sort()
print(lista_min[0])    
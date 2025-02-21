def bubble_sort(lista):
    n = len(lista)
    contador_it = 0
    for i in range(n):
        for j in range(n-1):
            contador_it += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(f'Iteraciones: {contador_it}') 
    return lista
lista_ordenada = bubble_sort([8, 6, 1, 4, 5, 33, 20004])
print(lista_ordenada)
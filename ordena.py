def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Testando o algoritmo
lista = [3,9,5,8,2,4,7,1,6,10]
print(f"Lista não ordenada {lista}")
print("Lista ordenada: ", bubble_sort(lista))
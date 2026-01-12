def znajdz_duplikaty(lista):
    licznik = {}
    duplikaty = []
    for elem in lista:
        licznik[elem] = licznik.get(elem, 0) + 1
        if licznik[elem] == 2:  # dodajemy tylko raz
            duplikaty.append(elem)
    return duplikaty

print(znajdz_duplikaty([1, 2, 3, 2, 4, 1, 5]))  # [1, 2]

import time
import random

def bubble_sort(lista):
    n = len(lista)
    arr = lista.copy()  # kopiujemy listę, żeby nie modyfikować oryginału
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test 1: Mała lista losowa
mala_lista = [random.randint(1, 100) for _ in range(50)]

# Test 2: Duża lista losowa
duza_lista = [random.randint(1, 1000) for _ in range(500)]

# Test 3: Prawie posortowana lista
prawie_posortowana = list(range(500))
for _ in range(5):
    i, j = random.randint(0, 499), random.randint(0, 499)
    prawie_posortowana[i], prawie_posortowana[j] = prawie_posortowana[j], prawie_posortowana[i]

def test_sortowania(funkcja, lista):
    start = time.time()
    wynik = funkcja(lista)
    end = time.time()
    return end - start, wynik

testy = [("Mała lista", mala_lista),
         ("Duża lista", duza_lista),
         ("Prawie posortowana", prawie_posortowana)]

algorytmy = [("Bubble Sort", bubble_sort), ("Merge Sort", merge_sort)]

for nazwa_alg, alg in algorytmy:
    print(f"\n--- {nazwa_alg} ---")
    for nazwa_test, lista_test in testy:
        czas, _ = test_sortowania(alg, lista_test)
        print(f"{nazwa_test}: {czas:.6f} sekundy")


def scal_listy(lista1, lista2):
    wynik = []
    i = j = 0
    n, m = len(lista1), len(lista2)

    while i < n and j < m:
        if lista1[i] <= lista2[j]:
            wynik.append(lista1[i])
            i += 1
        else:
            wynik.append(lista2[j])
            j += 1

    while i < n:
        wynik.append(lista1[i])
        i += 1

    while j < m:
        wynik.append(lista2[j])
        j += 1

    return wynik

print(scal_listy([1, 3, 5, 7], [2, 4, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print(scal_listy([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(scal_listy([1, 4, 7], [2, 3, 5, 6, 8, 9]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(scal_listy([], [1, 2, 3]))  # [1, 2, 3]
print(scal_listy([5, 10, 15], []))  # [5, 10, 15]
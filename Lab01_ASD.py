import string
from itertools import permutations

def zlam_haslo(prawdziwe_haslo):
    prawdziwe_haslo = str(prawdziwe_haslo)
    znaki = list(string.ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    proby = 0
    for i in range(len(znaki)):
        for j in range(len(znaki)):
            for k in range(len(znaki)):
                haslo = znaki[i] + znaki[j] + znaki[k]
                proby += 1
                if haslo == prawdziwe_haslo:
                    return "Znaleziono hasło \"" + haslo + "\" po " + str(proby) + " próbach."
    return None


def znajdz_trojke(lista, target):
    for i in range(len(lista)):
        for j in range(len(lista)):
            for k in range(len(lista)):
                if(lista[i] + lista[j] + lista[k] == target and i != j and i != k and j != k):
                    return (lista[i], lista[j], lista[k])
    return None


def komiwojazer():
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
        ]
    n = len(dist)
    miasta = list(range(n))
    start = 0
    min_droga = None
    min_dystans = float('inf')
    for p in permutations(miasta[1:]):
        droga = [start] + list(p) + [start]
        dystans = sum(dist[droga[i]][droga[i+1]] for i in range(n))
        if dystans < min_dystans:
            min_dystans  = dystans
            min_droga = droga
    return min_droga, min_dystans


print(zlam_haslo('h2o'))
print(znajdz_trojke((1,4,2,7,0),11))
print(komiwojazer())
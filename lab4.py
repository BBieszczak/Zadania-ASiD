# Zadanie 1
import heapq

def min_sal(wyklady):
    wyklady_sorted = sorted(wyklady, key=lambda x: x[1])

    heap = []
    next_room_id = 1

    assignment = {}

    for name, start, end in wyklady_sorted:
        if heap and heap[0][0] <= start:
            end_time, room_id = heapq.heappop(heap)
        else:
            room_id = next_room_id
            next_room_id += 1

        assignment[name] = room_id
        heapq.heappush(heap, (end, room_id))

    min_rooms = next_room_id - 1
    return min_rooms, assignment

wyklady = [
    ("Wykład A", 9, 10),
    ("Wykład B", 9, 11),
    ("Wykład C", 10, 12),
    ("Wykład D", 11, 13),
]

rooms, assignment = min_sal(wyklady)

print("Minimalna liczba sal:", rooms)
print("Przydział:")
for k, v in assignment.items():
    print(f"{k} → sala {v}")

# Zadanie 2
from collections import deque

def wydaj_reszte_bruteforce(amount, coins):
    queue = deque()
    queue.append((0, []))

    visited = set()
    visited.add(0)

    while queue:
        current_sum, combination = queue.popleft()

        for coin in coins:
            new_sum = current_sum + coin

            if new_sum > amount:
                continue

            new_combination = combination + [coin]

            if new_sum == amount:
                return new_combination

            if new_sum not in visited:
                visited.add(new_sum)
                queue.append((new_sum, new_combination))

    return None

print(wydaj_reszte_bruteforce(6, [1,3,4]))

# Zadanie 3

import heapq

def lacz_pliki(rozmiary):
    heap = rozmiary[:]
    heapq.heapify(heap)

    total_cost = 0
    merges = []

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        cost = a + b
        total_cost += cost
        merges.append((a, b, cost))

        heapq.heappush(heap, cost)

    return total_cost, merges

pliki = [20, 30, 10, 5]

cost, merges = lacz_pliki(pliki)

print("Minimalny koszt:", cost)
print("Sekwencja łączeń:")
for a, b, c in merges:
    print(f"{a} + {b} = {c}")

# Zadanie 4

from collections import defaultdict

def zaplanuj_dostawy(paczki, pojemnosc):
    """
    paczki: lista krotek (nazwa, rozmiar, deadline, wartosc)
    pojemnosc: maksymalna pojemnosc auta na dzien
    """

    # sortowanie: najpierw deadline, potem wartosc malejaco
    paczki_sorted = sorted(
        paczki,
        key=lambda x: (x[2], -x[3])
    )

    # harmonogram: dzien -> lista paczek
    harmonogram = defaultdict(list)
    # zajetosc: dzien -> aktualna zajeta pojemnosc
    zajetosc = defaultdict(int)

    for name, size, deadline, value in paczki_sorted:
        # próbujemy wstawić paczkę jak najpóźniej przed deadline
        for day in range(deadline, 0, -1):
            if zajetosc[day] + size <= pojemnosc:
                harmonogram[day].append(name)
                zajetosc[day] += size
                break
        # jeśli nie da się wstawić → paczka pominięta

    return dict(harmonogram)

paczki = [
    ("Paczka A", 5, 3, 100),
    ("Paczka B", 3, 2, 80),
    ("Paczka C", 4, 4, 120),
    ("Paczka D", 2, 2, 60),
]

pojemnosc_auta = 10

harmonogram = zaplanuj_dostawy(paczki, pojemnosc_auta)

for dzien in sorted(harmonogram):
    print(f"Dzień {dzien}: {harmonogram[dzien]}")
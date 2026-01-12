# Zadanie 1
import random

def est_div_by_7(attempts):
    res = 0
    for _ in range(attempts):
        x = random.randint(1, 100)
        if x % 7 == 0:
            res += 1

    return res

print("Estymowana liczba liczb podzielnych przez 7:", est_div_by_7(10))

# Zadanie 2
import math

def cena_laptopa(sklep_nr):
    # Symulowana funkcja ceny (nie zmieniaj)
    random.seed(sklep_nr)
    return 2000 + random.randint(-500, 500) + abs(sklep_nr - 42) * 5

def simulated_annealing(max_sklep=100, start_temp=1000, alpha=0.95, steps_per_temp=50):

    current = random.randint(0, max_sklep)
    current_cost = cena_laptopa(current)
    best = current
    best_cost = current_cost

    temp = start_temp

    while temp > 1:
        for _ in range(steps_per_temp):
            move = random.choice([-1, 1])
            neighbor = max(0, min(max_sklep, current + move))
            neighbor_cost = cena_laptopa(neighbor)

            if neighbor_cost < current_cost:
                current, current_cost = neighbor, neighbor_cost
            else:
                delta = neighbor_cost - current_cost
                if random.random() < math.exp(-delta / temp):
                    current, current_cost = neighbor, neighbor_cost

            if current_cost < best_cost:
                best, best_cost = current, current_cost

        temp *= alpha

    return best, best_cost

najtanszy_sklep, najtansza_cena = simulated_annealing()
print("Najtańszy sklep:", najtanszy_sklep)
print("Cena:", najtansza_cena)

# Zadanie 3

import random
import string

target = "PYTHON"
length = len(target)
pop_size = 100
mutation_rate = 0.1
generations = 1000

def random_individual():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def fitness(individual):
    return sum(1 for i, c in enumerate(individual) if c == target[i])

def crossover(parent1, parent2):
    point = random.randint(1, length-1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual):
    individual = list(individual)
    for i in range(length):
        if random.random() < mutation_rate:
            individual[i] = random.choice(string.ascii_uppercase)
    return ''.join(individual)

population = [random_individual() for _ in range(pop_size)]

for gen in range(generations):
    population.sort(key=fitness, reverse=True)
    if fitness(population[0]) == length:
        print(f"Znaleziono w generacji {gen}: {population[0]}")
        break

    new_population = population[:10]
    while len(new_population) < pop_size:
        parent1, parent2 = random.choices(population[:50], k=2)
        child = mutate(crossover(parent1, parent2))
        new_population.append(child)

    population = new_population
else:
    print("Nie znaleziono idealnego słowa, najlepsze:", population[0])

# Zadanie 5

def estimate_integral(n_samples):
    count_under_curve = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if y <= x**2:
            count_under_curve += 1

    return count_under_curve / n_samples

result = estimate_integral(1000)
print(f"Przybliżone pole pod krzywą y=x^2 w [0,1]: {result}")
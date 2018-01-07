from Functions import *

population = StartPopulation(100)
mutationRate = 0.05

random_starting_pop = choose(population)

for x in range(0, 100):
    tournament(population)
    population = nextGen(population, mutationRate)
    print(findBest(population))

best_end_pop = findBest(population)

print(random_starting_pop, best_end_pop)

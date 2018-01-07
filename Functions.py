from time import time
from Classes import *

def StartPopulation(total):
    population = []

    for ind in range(0, total):
        sword_length = random.randint(2, 5)
        speed = random.randint(4, 15)
        evade = random.random()
        strength = random.randint(4, 15)
        health = random.randint(10, 50)

        population.append(DNA(
        sword_length,
        speed,
        evade,
        strength,
        health))

    print("done")

    return population


def fight(indA, indB):
    tstart = time()
    healthA = indA.health
    healthB = indB.health

    def attack(health, ind1, ind2):
        global count
        #ind1 attacks ind2
        if ind2.evade > random.random() * ind1.sword_length:
            #B evades
            pass
        else:
            health -= ind1.strength

        return health


    while time() - tstart < 0.005:
        if indA.speed >= indB.speed:
            #A starts to attack
            healthB = attack(healthB, indA, indB)
            if healthB <= 0:
                indA.fitness += 1
                break

            healthA = attack(healthA, indB, indA)
            if healthA <= 0:
                indB.fitness += 1
                break

        else:
            #B starts to attack
            healthA = attack(healthA, indB, indA)
            if healthA <= 0:
                indB.fitness += 1
                break

            healthB = attack(healthB, indA, indB)
            if healthB <= 0:
                indA.fitness += 1
                break

    #If they manage to evade each other's attacks
    indA.fitness += 1
    indB.fitness += 1



def tournament(population):
    """Tournament where all individuals fight between each other"""
    for A in range(0, len(population)):
        for B in range(0, len(population)):
            if A != B:
                fight(population[A], population[B])



def subWith0min(a, b):
    if a-b<0:
        return 0
    return a-b


def choose(l):
    i = random.randint(0, len(l) - 1)
    return l[i]



def nextGen(population, rate):
    """Creates the next generation"""
    newPopulation = []
    pop = []

    for ind in population:
        for x in range(0, ind.fitness):
            pop.append(ind)

    for n in range(0, len(population)):
        #Randomly choose the individual
        ind = choose(pop)
        #Cross Over
        seq = ind.crossOver(choose(pop))

        new_ind = DNA(seq[0], seq[1], seq[2], seq[3], seq[4])

        #Mutation
        new_ind.mutate(rate)
        #New individual formed!
        newPopulation.append(new_ind)


    return newPopulation





def findBest(population):
    best = population[0]
    for ind in population:
        if ind.fitness > best.fitness:
            best = ind

    return best

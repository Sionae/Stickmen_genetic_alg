import random
import pygame
from pygame.locals import *

pygame.init()

class DNA:
    """DNA class in which the genetic information of each object is stored"""

    def __init__(self, sword_length, speed, evade, strength, health):
        self.sword_length = sword_length #Will determine the range of touch
        self.speed = speed #Will determine the speed of the stickman
        #i.e. his capacity to attack first
        self.evade = int(evade * 1000)/1000
        self.strength = strength #Will determine the damage done
        self.health = health

        #Individual initial fitness
        self.fitness = 0



        self.sequence = [self.sword_length, self.speed, self.evade,
                        self.strength, self.health]


    def mutate(self, rate):
        """Mutation function"""

        if random.random() <= rate:
            TraitToChange = random.randint(0, len(self.sequence) - 1)

            if random.random() <= 0.5:  #1/2 chance to decrease
                c = random.randint(1, 5)
            else: #1/2 chance to increase
                c = random.randint(1, 5)

            self.sequence[TraitToChange] *= c #Implementing the change

            if self.sequence[TraitToChange] < 0: #Don't let the value be under 0
                self.sequence[TraitToChange] = abs(self.sequence[TraitToChange])
            elif self.sequence[TraitToChange] == 0: #If it's 0, it may cause problems
                self.sequence[TraitToChange] += 0.5

        return self.sequence


    def crossOver(self, other):
        """Cross Over function"""

        if other.sequence == self.sequence:
            return self.sequence

        newSequence = []

        infFromSelf = random.randint(0, len(self.sequence))


        for inf in range(0, infFromSelf):
            newSequence.append(self.sequence[inf])

        for inf in range(infFromSelf, len(other.sequence)):
            newSequence.append(other.sequence[inf])

        return newSequence


    def __repr__(self):
        return str(self.sequence)


    def draw(self, window, pos):


        font = pygame.font.SysFont("Arial", 14)
        text = font.render("Sword length:" + str(self.sword_length) + "\n"
                        + "Speed:" + str(self.speed) + "\n"
                        + "Evade:" + str(self.evade) + "\n"
                        + "Strength:" + str(self.strength) + "\n"
                        + "Health:" + str(self.health), 1, (255, 255, 255))

        window.blit(text, pos)

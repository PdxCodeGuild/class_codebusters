"""
Mob Programming: Jackalope Simulator
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.

Version 2
Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

name
age
sex
whether they're pregnant
Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.
"""
import random


class Jackalope:
    def __init__(self, name, sex):
        self.name = name
        self.age = 0
        self.sex = sex
        self.pregnant = False

    def can_mate(self):
        if self.pregnant == False and 4 <= self.age <= 8:
            return True
        else:
            return False


def name():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    return (random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)).title()


sex = ['male', 'female']


def let_there_be_jackalopes(population=2):
    census = []
    for i in range(population):
        census.append(Jackalope(name(), sex[i % 2]))
    return census


def reaper(jackalopes):
    population = []
    for jack in jackalopes:
        if jack.age < 11:
            population.append(jack)
    return population


jack_pop = let_there_be_jackalopes()
year = 0
while 1 < len(jack_pop) < 1000:
    year += 1
    random.shuffle(jack_pop)
    # print(len(jack_pop))

    jack_pop = reaper(jack_pop)
    for i in range(len(jack_pop)):
        jack = jack_pop[i]
        jack.age += 1

        if jack.pregnant:
            jack_pop.extend([Jackalope(name(), random.choice(sex)),
                            Jackalope(name(), random.choice(sex))])
            jack.pregnant = False

        if jack.sex == "female" and jack.can_mate:
            left = jack_pop[i-1]
            right = jack_pop[i+1] if i+1 < len(jack_pop)-1 else None

            if left.sex == 'male' and left.can_mate():
                jack.pregnant = True

            elif right and right.sex == 'male' and right.can_mate():
                jack.pregnant = True

print(year)
print(len(jack_pop))

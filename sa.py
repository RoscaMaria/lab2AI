import math
import random
import numpy as np
import time
import functions

def calculateDist(x1: int, y1: int, x2: int, y2: int):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def fitness(orase: {}, permutare: list):
    sum = calculateDist(orase[permutare[0]][0], orase[permutare[0]][1], orase[permutare[len(permutare)-1]][0], orase[permutare[len(permutare)-1]][1])
    for index in range(len(permutare) - 1):
        dist = calculateDist(orase[permutare[index]][0], orase[permutare[index]][1], orase[permutare[index + 1]][0], orase[permutare[index + 1]][1])
        sum = sum + dist
    return sum


def twoRandomNumbers(size):
    n1 = random.randint(0, size)
    n2 = random.randint(0, size)

    while n1 == n2:
        n2 = random.randint(0, 99)

    return [n1, n2]


def twoSwap(permutare):
    index = twoRandomNumbers(len(permutare) - 1)

    aux = permutare[index[0]]
    permutare[index[0]] = permutare[index[1]]
    permutare[index[1]] = aux

    return permutare


def randomStatistic():
    s = random.random()
    while s == 1:
        s = random.random()
    return s


def SimulatedAnnealing(iteratii, temperatura, tmin, alfa, orase):
    c = np.random.permutation(len(orase))
    f = fitness(orase, c)
    i = iteratii
    while temperatura > tmin:
        iteratii = i
        print(i)
        while iteratii > 0:
            vecin = twoSwap(c)
            print(vecin)
            fvecin = fitness(orase, vecin)
            delta = fvecin - f
            if delta < 0:
                c = vecin
            else:
                if random.random() < math.exp(-delta / temperatura):
                    c = vecin
            iteratii = iteratii - 1

        temperatura = alfa * temperatura
        print(temperatura)
    return c


def executii(iteratii, nr_executii, temperatura, tmin, orase, alfa, filename):
    exect = 0
    solutii = []
    timp = []
    while exect < nr_executii:
        start_time = time.time()
        solutie = SimulatedAnnealing(iteratii, temperatura, tmin, alfa, orase)
        f = fitness(orase, solutie)
        solutii.append([solutie, f])
        timp.append(start_time)
        exect = exect + 1
    functions.writeSA(filename, iteratii, nr_executii, temperatura, tmin, alfa, solutii, timp)
    print("gata")

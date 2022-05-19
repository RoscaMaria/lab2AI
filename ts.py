import numpy as np
import time
import functions


def vecin(array, index):
    a = array[:]
    if a[index] == 0:
        a[index] = 1
    else:
        a[index] = 0
    return a


# valideaza o solutie a problemei - verifica daca greutatea obiectelor nu depaseste greutatea maxima
def validateArray(array, objects, value):
    sum = 0
    for i in range(len(array)):
        if array[i] == 1:
            sum += objects[i][1]
        if sum > value:
            return False
    return True


# returneaza o solutie valida a problemei
def validSolution(obj):
    randomArray = np.random.choice([0, 1], size=(obj[2],))
    while not validateArray(randomArray, obj[0], obj[1]):
        randomArray = np.random.choice([0, 1], size=(obj[2],))
        print(randomArray)

    return randomArray


# functia de fitness: returneaza valoarea obiectelor daca acestea nu depasesc greutatea data
def fitness(array, objects, value):
    gr: int = 0
    valoare = 0
    for i in range(len(array)):
        if array[i] == 1:
            gr = gr + objects[i][1]
            valoare = valoare + objects[i][0]
    if gr > value:
        return -1
    return valoare


def initMemory(size: int):
    memory = []
    for i in range(size):
        memory.append(0)
    return memory


def updateMemory(memory):
    for i in range(len(memory)):
        if memory[i] != 0:
            memory[i] = memory[i] - 1


def bestSol(array, obj, sol, memory):
    maxf = sol
    maxVec = array[:]
    pos = -1
    for i in range(len(array)):
        if memory[i] == 0:
            vec = vecin(array, i)
            f = fitness(vec, obj[0], obj[1])
            if f > maxf:
                maxf = f
                maxVec = vec[:]
                pos = i

    return maxVec, maxf, pos


# returneaza cea mai buna solutie dintre cele toate gasite
def returnBestSolution(solutii):
    max = [[], -1]
    for i in range(len(solutii)):
        if solutii[i][1] > max[1]:
            max = solutii[i]

    return max


def TabuSearch(iteratii, nr_executii, tabuNumber, obj, filename):
    # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte

    bestSolutions = []
    times = []
    exect = 0

    while exect < nr_executii:
        solutii = []
        start_time = time.time()
        c = validSolution(obj)
        memory = initMemory(obj[2])
        j: int = 0

        while j < iteratii:
            sol = fitness(c, obj[0], obj[1])
            rez = bestSol(c, obj, sol, memory)
            x = rez[0]
            f = rez[1]
            i = rez[2]

            updateMemory(memory)
            if j != 0 and i != -1:
                memory[i] = tabuNumber

            c = x
            solutii.append([x, f])
            j += 1

        print(solutii)
        print(returnBestSolution(solutii))
        bestSolutions.append(returnBestSolution(solutii))
        times.append(start_time)
        exect = exect + 1
    functions.write(filename, iteratii, nr_executii, tabuNumber, bestSolutions, times)

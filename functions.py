# citeste obiectele din fisier
# returneaza : # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte
def read(filename):
    f = open(filename, "r")
    s = f.readline()
    numObjs = int(s)
    value = 0
    objects = []
    while s:
        x = s.split()
        if len(x) > 1:
            objects.append([int(x[1]), int(x[2])])
        else:
            if len(x) == 1:
                value = int(x[0])
        s = f.readline()
    f.close()
    return objects, value, numObjs


# scrie in fisier pentru hill climbing
def write(filename, k, nr_executii, tabu,  solutii, timp):
    mean = 0
    meanTime = 0
    f = open(filename, "a")
    f.write("iteratii = " + str(k) + " nr_executii = " + str(nr_executii) + " nr_tabu = " + str(tabu) + "\n")
    for i in range(len(solutii)):
        f.write(str(solutii[i][0]) + " " + str(solutii[i][1]) + " " + str(timp[i]) + "\n")

        mean = mean + solutii[i][1]
        meanTime = meanTime + timp[i]
    mean = mean / len(solutii)
    meanTime = meanTime / len(solutii)
    f.write(str(mean) + "\n")
    f.write(str(meanTime) + "\n\n")

    f.close()


# returneaza : # obj[0] - lista obiecte, obj[1] - valoare maxima, obj[2] - nr obiecte
def readSA(filename):
    f = open(filename, "r")
    objects = {}
    s = f.readline()
    while s:
        x = s.split()
        objects[int(x[0]) - 1] = [int(x[1]), int(x[2])]
        s = f.readline()
    f.close()
    return objects


def writeSA(filename, k, nr_executii, t, tmin, alfa, solutii, timp):
    mean = 0
    meanTime = 0
    f = open(filename, "a")
    f.write(
        "iteratii = " + str(k) + " nr_executii = " + str(nr_executii) + " temperatura = " + str(t) + " tempMin = " + str(
            tmin) + " alfa = " + str(alfa) + "\n")
    for i in range(len(solutii)):
        f.write(str(solutii[i][0]) + " " + str(solutii[i][1]) + " " + str(timp[i]) + "\n")
        mean = mean + solutii[i][1]
        meanTime = meanTime + timp[i]
    mean = mean / len(solutii)
    meanTime = meanTime / len(solutii)
    f.write(str(mean) + "\n")
    f.write(str(meanTime) + "\n\n")

    f.close()

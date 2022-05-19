import functions
import ts
import sa


def optiuni():
    print("1. Tabu Search rucsac 5 obiecte\n"
          "2. Tabu Search rucsac 20 obiecte\n"
          "3. Tabu Search rucsac 200 obiecte\n"
          "4. Simulated Annealing kroB100.tsp (6)\n"
          "0. Exit\n"
          )


def meniu():
    optiuni()
    opt = int(input("Optiune:\n"))
    a = 0.000001
    print(a)
    while opt != 0:
        if opt == 1:
            k = int(input("Numarul iteratiilor:\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            tabuNumber = int(input("Numarul de iteratii tabu:\n"))
            obj = functions.read("rucsac-5")
            ts.TabuSearch(k, nr_executii, tabuNumber, obj, "solutiiTS5.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 2:
            k = int(input("Numarul iteratiilor:\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            tabuNumber = int(input("Numarul de iteratii tabu:\n"))
            obj = functions.read("rucsac-20.txt")
            ts.TabuSearch(k, nr_executii, tabuNumber, obj, "solutiiTS20.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 3:
            k = int(input("Numarul iteratiilor:\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            tabuNumber = int(input("Numarul de iteratii tabu:\n"))
            obj = functions.read("rucsac-200.txt")
            ts.TabuSearch(k, nr_executii, tabuNumber, obj, "solutiiTS200.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 4:
            k = int(input("Numarul iteratiilor:\n"))
            nr_executii = int(input("Numarul de executii:\n"))
            t = int(input("Temperatura:\n"))
            tmin = float(input("Temperatura minima:\n"))
            alfa = float(input("Alfa:\n"))
            orase = functions.readSA("kroB100.tsp")
            sa.executii(k, nr_executii, t, tmin, orase, alfa, "SA.txt")
            print("done\n")
            opt = int(input("Optiune:\n"))


# meniu()

def main():
    # orase = functions.readSA("kroB100.tsp")
    # #sa.SimulatedAnnealing(2, 10, 0.00001, 0.99, orase)
    # sa.executii(10, 5, 100000, 0.00001, orase, 0.77, "SA.txt")

    #obj = functions.read("rucsac-5.txt")
    # f = ts.fitness([1, 1, 0, 0, 1], obj[0], obj[1])
    # rez = ts.bestSol([1, 1, 0, 0, 1], obj, f, [0, 0, 0, 0, 0])
    #print(rez)
    pass


meniu()

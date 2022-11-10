import random

inceput = False

index = 0


cuvinteRandomizate = []
cuvinte = []
frecventa = {}

def asiguraInit():
    global cuvinte
    global frecventa
    if len(cuvinte) < 1:
        with open("date/cuvinte.txt", "r") as f:
            cuvinte = [line.rstrip() for line in f]
            global cuvinteRandomizate
            cuvinteRandomizate = cuvinte.copy()
            random.shuffle(cuvinteRandomizate)
        cuvstr = "".join(cuvinte)
        for i in range(65, 91):
            caracter = chr(i)
            frecventa[caracter] = cuvstr.count(caracter)

        frecventa = {k: v for k, v in sorted(frecventa.items(), key=lambda item: item[1], reverse=True)}

def getFrecventa():
    asiguraInit()

    global frecventa
    return frecventa

def getCuvinte():
    asiguraInit()

    global cuvinte
    return cuvinte

def getIndex():
    global index
    return index

def getCuvantCurent():
    asiguraInit()
    global index
    global cuvinteRandomizate
    return cuvinteRandomizate[index]

def nextCuvant():
    asiguraInit()
    global index
    index += 1
    if index >= len(getCuvinte()):
        resetJoc()

def resetJoc():
    global index
    global cuvinteRandomizate
    random.shuffle(cuvinteRandomizate)
    index = 0

    

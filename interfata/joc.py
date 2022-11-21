import os
import pickle
import random
import json
from collections import Counter, defaultdict

index = 0

cuvinteRandomizate = []
cuvinte = []


def asiguraInit():
    global cuvinte

    if len(cuvinte) < 1:
        with open("date/cuvinte.txt", "r") as f:
            cuvinte = [line.rstrip() for line in f]
                
            global cuvinteRandomizate
            cuvinteRandomizate = cuvinte.copy()
            random.shuffle(cuvinteRandomizate)


def calc_rasp(input, cuvant):
    gresite = [i for i, v in enumerate(input) if v != cuvant[i]]
    gas = Counter(cuvant[i] for i in gresite)
    rasp = [2] * 5
    for i in gresite:
        car = input[i]
        if gas[car] > 0:
            rasp[i] = 1
            gas[car] -= 1
        else:
            rasp[i] = 0
    return tuple(rasp)

def gen_lista_rasp(ls):
    ls_rasp = {}
    for cuv in ls:
        for cuv1 in ls:
            rasp = "".join([str(c) for c in calc_rasp(cuv, cuv1)])
            
            if not cuv in ls_rasp.keys():
                ls_rasp[cuv] = {}

            if not rasp in ls_rasp[cuv].keys():
                ls_rasp[cuv][rasp] = []
            
            ls_rasp[cuv][rasp].append(cuv1)
        print(ls_rasp[cuv])
    return json.dumps(ls_rasp)

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
    asiguraInit()

    global index
    global cuvinteRandomizate
    random.shuffle(cuvinteRandomizate)
    index = 0

    

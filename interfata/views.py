from distutils import core
import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template import loader

from interfata.joc import calc_rasp, getCuvinte, getIndex, getCuvantCurent, nextCuvant, resetJoc


def index(request):
    resetJoc()

    template = loader.get_template('index.html')

    context = {
        'cuv': getCuvinte(),
        'i': getIndex(),
    }
    return HttpResponse(template.render(context, request))

def reset(request):
    resetJoc()
    return HttpResponse()

def feedback(request):
    if not request.body:
        return HttpResponseBadRequest()
    input = json.loads(request.body)["cuv"]
    if not input in getCuvinte():
        print("NU E", input)
        return JsonResponse({
            "corecte": [],
            "partiale": [],
        }, safe = False)
    cuvant = getCuvantCurent()
    print(input, cuvant)
    pattern = calc_rasp(input, cuvant)
    corecte = []
    for i in range(len(pattern)):
        if pattern[i] == 2:
            corecte.append(i)
    
    if len(corecte) == 5:
        nextCuvant()

    print("".join([str(c) for c in pattern]))
    
    return JsonResponse({
        "pattern": "".join([str(c) for c in pattern]),
        "corecte": corecte,
        "i": getIndex()
    }, safe = False)
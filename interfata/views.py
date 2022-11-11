from distutils import core
import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template import loader

from interfata.joc import getFrecventa, getCuvinte, getIndex, getCuvantCurent, nextCuvant, resetJoc, getBiti


def index(request):
    template = loader.get_template('index.html')

    context = {
        'frecv': getFrecventa(),
        'cuv': getCuvinte(),
        'i': getIndex(),
        'biti': getBiti()
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
        return JsonResponse({
            "corecte": [],
            "partiale": [],
        }, safe = False)
    cuvant = getCuvantCurent()
    print(input, cuvant)
    corecte = []
    partiale = []
    for i in range(0, 5):
        if input[i] == cuvant[i]:
            corecte.append(i)
            nou = list(cuvant)
            nou[i] = '_'
            cuvant = ''.join(nou)
    for i in range(0, 5):
        if input[i] in cuvant:
            cuvant = cuvant.replace(input[i], "_", 1)
            partiale.append(i)

    if len(corecte) == 5:
        nextCuvant()
    
    return JsonResponse({
        "corecte": corecte,
        "partiale": partiale,
        "i": getIndex()

    }, safe = False)
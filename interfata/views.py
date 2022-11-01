from distutils import core
import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template import loader

from interfata.joc import getFrecventa, getCuvinte, getIndex, getCuvantCurent


def index(request):
    template = loader.get_template('index.html')

    context = {
        'frecv': getFrecventa(),
        'cuv': getCuvinte(),
        'i': getIndex(),
    }
    return HttpResponse(template.render(context, request))

def feedback(request):
    if not request.body:
        return HttpResponseBadRequest()
    input = json.loads(request.body)["cuv"]
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
            partiale.append(i)
    
    return JsonResponse({
        "corecte": corecte,
        "partiale": partiale,

    }, safe = False)
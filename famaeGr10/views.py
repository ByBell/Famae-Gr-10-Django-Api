from django.http import HttpResponse, JsonResponse

def essai(request, zipcode):

    dummyDict = {'Debug': zipcode}

    return JsonResponse(dummyDict)
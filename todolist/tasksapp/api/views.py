from django.http import JsonResponse


def getRoutes(request):

    # show all the endpoints
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return JsonResponse(routes, safe=False)
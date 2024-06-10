from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Django REST framework JSON Web Token Authentication - Simple JWT
# What is the difference? Why choose this?


@api_view(['GET']) # this takes http method we can set
def getRoutes(request):

    # show all the endpoints
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)
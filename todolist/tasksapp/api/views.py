from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Django REST framework JSON Web Token Authentication - Simple JWT
# What is the difference? Why choose this?


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET']) # this takes http method we can set
def getRoutes(request):

    # show all the endpoints
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)
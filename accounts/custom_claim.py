from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import requires_csrf_token
class my_token_obtain_per_serializer(TokenObtainPairSerializer):
    @requires_csrf_token
    @classmethod
    def get_token(cls, user):
        token=super().get_token(user)
        token["username"]=user.username
        token["email"]=user.email
        token["pasword"]=user.password

        return token

class my_token_optain_per_view(TokenObtainPairView):
    serializer_class=my_token_obtain_per_serializer
    
        
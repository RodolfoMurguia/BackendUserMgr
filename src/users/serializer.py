#importamos librerias para usar serializers
from rest_framework import serializers
from .models import  user
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class loginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=30)

    #def userValidate():

    #Creamos el usuario y generamos su token correspondiente
    def createUser(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token = Token.objects.create(user = user)

        return user, Token.key

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('userId', 
                'user',
                'password', 
                'email', 
                'firstName',
                'lastName',
                'isAdmin')


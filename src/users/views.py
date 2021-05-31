from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response as resp
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.authentication import  TokenAuthentication
from django.contrib.auth.models import User

from .models import user
from .serializer import userSerializer, loginSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
    authentication_classes = (TokenAuthentication,)
    permissionClasses = (AllowAny,)# IsAuthenticated
    #Cambiar este parametro a IsAuthenticated

    def loginUser(self, request, *args):
        #Iniciamos sesion

        serializer = loginSerializer(req = request.data)
        serializer.is_valid(raise_exception=True)

        userId, tokenData  = serializer.save()

        userData = {
            'userId': userSerializer(user).data,
            'accessToken': tokenData
        }

        return resp(userData, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def createUser(self, request):
        #Validamos que vengan los elementos principales como mail, pass y username
        if 'user' in request.data:
            username = request.data['userId']
            password = request.data['userId']
            email = request.data['userId']
            nombre = request.data['userId']
            apellido = request.data['userId']
            isAdmin = request.data['userId']

            try:
                user.user = username
                user.password = password
                user.email = email
                user.firstName = nombre
                user.lastName = apellido
                user.isAdmin = isAdmin
                #Intentamos almacenar
                user.save()
                # enviamos a serializer para formatear 
                serializer = userSerializer(user, many=False)
                responseData = {'message': "Se ha creado el usuario " + username, 'result': serializer.data}
                #Retornamos respuesta
                return resp(responseData, status = status.HTTP_201_CREATED)

            except:
                responseData = {'message': "Ha ocurrido un error"}
                #Retornamos respuesta
                return resp(responseData, status = status.HTTP_409_CONFLICT)

        else:
            responseData = {'message': "No cuentas con un nombre de usuario valido"}
            #Retornamos respuesta
            return resp(responseData, status = status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
import json


class UserView(View):
    def post(self, request):
        """
        expected input:
        {
            "user": "",
            "password": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        }

        expected output:
        {  
            "pk": "",
            "user": "",
            "email": "",
            "first_name": "",
            "last_name": ""
        }

        bonus: revisar que el usuario exista
        si existe retorna el usuario existe en el formato esperado de respuesta.
        """
        
        # puedes borrar esta parte de código
        data = dict(
            user="dummy",
            email="dummy@worky.mx"
        )

        data = json.dumps(data)

        return HttpResponse(data)


#genero Importaciones

from rest_framework import viewsets

from .models import user
from .serializer import userSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
#importamos librerias y viewsets
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import userViewSet

#Genero el enrutamiento

router = routers.SimpleRouter()
router.register('users', userViewSet)
#router.register('users', userViewSet)
#router.register('users', userViewSet)

urlpatterns = router.urls


from django.urls import path,include
from login.views import acceder, home, salir

urlpatterns = [
  path('login/', acceder, name = "login"),
  path('', home, name="home"),
  path('logout/', salir, name="logout"),
]
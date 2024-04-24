from django.urls import path
from recipes.views import sobre, home, contato

urlpatterns = [
    path('sobre/', sobre),
    path('home/', home),
    path('contato/', contato),
]

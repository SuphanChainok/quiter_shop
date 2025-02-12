from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name= 'login'),
    path("index/", views.indax, name= 'index'),
    path("classic/", views.classic, name= 'classic'),
    path("quiter/", views.quiter, name= 'quiter')
]


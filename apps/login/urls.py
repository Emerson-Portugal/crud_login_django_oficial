#app.login/urls.py
from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.home, name='home'), 
    path('logout/', views.exit, name='exit' ),
]
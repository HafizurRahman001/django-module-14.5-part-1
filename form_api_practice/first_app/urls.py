from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('django_form/', views.DjangoForm, name='django_form'),
]
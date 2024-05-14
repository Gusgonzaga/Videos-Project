from django.urls import path
from djangoProject.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato', views.contact, name='contact'),
]
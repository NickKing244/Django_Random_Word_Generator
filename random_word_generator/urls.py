from django.urls import path     
from . import views


urlpatterns = [
    path('', views.random_word),
    path('reset', views.reset),
    path('random_word', views.random_word),
]

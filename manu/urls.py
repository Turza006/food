
from django.urls import path

from . import views

urlpatterns = [

    path('manu', views.manu, name ='manu'),
    path('<int:manu_id>/', views.show, name='show'),
]
from django.urls import path
from . import views

urlpatterns = [

    # localhost:8000/
    path('', views.GameView.as_view(), name='game'),
]
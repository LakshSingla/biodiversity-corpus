from django.urls import path

from . import views

app_name = 'tweets'

urlpatterns = [
    path('<str:keyword>/', views.tweets, name='index'),
]
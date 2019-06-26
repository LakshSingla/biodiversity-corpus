from django.urls import path

from . import views

app_name = 'db'

urlpatterns = [
    path('categories/', views.category, name='index'),
    path('subcategories/', views.sub_category, name='index'),
]
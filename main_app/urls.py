from django.urls import path #need path func to define each route
from . import views #need thees to map routes to view funcs/classes (kinda like controllers)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('lists/', views.lists_index, name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.points_list, name='points_list'),
    path('add_point/', views.add_point, name='add_point'),
]


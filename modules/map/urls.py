from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.points_list, name='points_list'),
    path('add_point/', views.add_point, name='add_point'),
    path('toggle_favorite/<int:point_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorite_points/', views.favorite_points, name='favorite_points'),
]


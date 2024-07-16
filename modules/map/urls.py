from django.urls import path
from . import views
from .views import CommentCreateView, PointsListView

urlpatterns = [
    path('home/', PointsListView.as_view(), name='points_list'),
    path('add_point/', views.add_point, name='add_point'),
    path('toggle_favorite/<int:point_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorite_points/', views.favorite_points, name='favorite_points'),
    path('points/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create_view'),
]


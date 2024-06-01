from django.urls import path, include
from . import views

urlpatterns = [
    # post views
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.dashboard, name='dashboard'),
]


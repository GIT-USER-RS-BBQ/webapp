from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('api/register/', views.RegisterView.as_view(), name='api_register'),
    path('matches/', views.get_matches, name='matches'),
    path('match/', views.get_match, name='match')
]
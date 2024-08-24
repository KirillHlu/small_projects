from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.news_home, name='news-home'), 
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('create_article/', views.create_article, name='create_article'),
    path('accounts/profile/', views.news_home, name='news-home'),
]

from django.urls import path
from .import views 
urlpatterns = [
    path('', views.home,name='home'),
     path('create_post/', views.create_post, name='create_post'),
    path('register/', views.register,name='register'),
     path('profile/', views.profile,name='profile'),
    path('login/', views.Login,name='login'),
    path('logout/', views.Logout,name='logout'),
     path('post/<slug:slug>/', views.detail, name='detail'),
]

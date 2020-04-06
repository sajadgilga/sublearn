from django.urls import path
from django.contrib.auth import views as auth_views

from users import views

app_name="users"

urlpatterns = [
    path('', views.user_home),
    path(r'register/', views.user_register, name="register"),
    path(r'login/', auth_views.LoginView.as_view(template_name='home/login.html'), name="login"),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name="logout"),
]

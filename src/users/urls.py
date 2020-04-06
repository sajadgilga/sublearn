from django.urls import path

from users import views

app_name="users"

urlpatterns = [
    path('', views.user_home),
    path(r'register/', views.user_register, name="register"),
    path(r'login/', views.user_login, name="login")
]

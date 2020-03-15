from django.urls import path

from users import views

urlpatterns = [
    path(r'signup/', views.user_test),
    path(r'login/', views.user_test)
]

from django.urls import path

from subtitles import views

app_name="subtitles"

urlpatterns = [
    path('', views.sub_processor, name='sub_processor'),
]

from django.urls import path
from .views import home

app_name="apache_age_app"

urlpatterns = [
    path('', home, name="home"),
]
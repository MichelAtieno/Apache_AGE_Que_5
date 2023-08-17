from django.urls import path
from .views import home, login_user

app_name="apache_age_app"

urlpatterns = [
    path('', home, name="home"),
    path('login_user',login_user, name="login"),
]
from django.urls import path
from .views import home, login_user, logout_user
from django.conf import settings
from django.conf.urls.static import static

app_name="apache_age_app"

urlpatterns = [
    path('', home, name="home"),
    path('login_user',login_user, name="login"),
    path('logout_user',logout_user, name="logout"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
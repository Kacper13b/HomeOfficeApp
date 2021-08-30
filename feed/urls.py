from django.urls import path
from django.conf.urls import include, url
from . import views
app_name = "feed"


urlpatterns = [
    path("", views.HomePage.as_view(), name='index'),
]
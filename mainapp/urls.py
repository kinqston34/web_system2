from django.urls import re_path as url
from mainapp import views,apps

app_name = apps.MainappConfig.name
urlpatterns = [
    url("^$",views.index,name="index"),
    url("^login",views.login,name="login"),
]

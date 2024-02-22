from django.urls import re_path as url
from mainapp import views

urlpatterns = [
    url("^index",views.index,name="index"),
    url("^login",views.login,name="login"),
]

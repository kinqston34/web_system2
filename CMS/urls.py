from django.urls import re_path as url
from CMS import views

urlpatterns = [
    url("^CMS/",views.index,name='index')
]

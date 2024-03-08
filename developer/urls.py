from django.urls import re_path as url
from developer import views,apps


app_name = apps.DeveloperConfig.name
urlpatterns = [
    url("^developer/$",views.developer,name="developer"), 
    url("^developer/login",views.login,name="login"),
    url("^developer/logout",views.logout,name="logout"),
    url("^developer/create",views.createdeveloper,name="createdeveloper"),
]
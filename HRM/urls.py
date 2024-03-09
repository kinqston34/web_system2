from django.urls import re_path as url
from HRM import views,apps

app_name = apps.HrmConfig.name
urlpatterns = [
    url("HRM/$",views.index,name="index"),
    url("HRM/login",views.login,name="login"),
    url("HRM/logout",views.logout,name="logout"),
    url("HRM/employee",views.employee,name="employee"),
    url("HRM/new_employee",views.new_employee,name="new_employee"),
    url("HRM/staff",views.staff,name="staff"),
    url("HRM/food_order",views.food_order,name="food_order"),
]

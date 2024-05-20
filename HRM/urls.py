from django.urls import re_path as url
from HRM import views,apps

app_name = apps.HrmConfig.name
urlpatterns = [
    url("^HRM/login",views.login,name="login"),
    url("^HRM/logout",views.logout,name="logout"),
    url("^HRM/$",views.employee,name="employee"),
    url("^HRM/new_employee/$",views.new_employee,name="new_employee"),
    url("^HRM/new_employee/HR_create",views.new_employee,name="HR_create"),
    url("^HRM/new_employee/base/$",views.new_employee,name="base"),
    # url("^HRM/new_employee/base/search",views.search_employee,name="search_employee_from_base"),
    url("^HRM/new_employee/base/query",views.search_employee_db,name="search_employee_from_base2"),
    url("^HRM/search_employee/$",views.search_employee,name="search_employee"),
    url("^HRM/search_employee/query",views.search_employee_db,name="search_employee_2"),
    url("^HRM/staff",views.staff,name="staff"),
    url("^HRM/staff/balance",views.staff,name="balance"),
    url("^HRM/staff/order_requirement",views.staff,name="order_requirement"),
    url("^HRM/resign",views.resign,name="resign"),
    
]

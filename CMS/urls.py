from django.urls import re_path as url
from CMS import views,apps

app_name = apps.CmsConfig.name
urlpatterns = [
    url("^CMS/$",views.index,name='index'), #首頁
    url("^CMS/login/",views.login,name='login'), #登入
    url("^CMS/logout/",views.logout,name='logout'), #登出
    url("^CMS/inventory/",views.inventory,name="inventory"),   # 庫存管理
    url("^CMS/material_supply/",views.material_supply,name="material_supply"),   #原料供應商管理
    url("^CMS/order/",views.order,name="order"), #訂單管理
    url("^CMS/HR/",views.HR,name="HR"), # 人事管理
    url("^CMS/food_supply/",views.food_supply,name="food_supply"), # 餐點供應商管理
    
]

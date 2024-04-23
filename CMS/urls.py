from django.urls import re_path as url
from CMS import views,apps

app_name = apps.CmsConfig.name
urlpatterns = [
    url("^CMS/$",views.index,name='index'), #首頁
    url("^CMS/login/",views.login,name='login'), #登入
    url("^CMS/logout/",views.logout,name='logout'), #登出
    url("^CMS/inventory/$",views.inventory,name="inventory"),   # 庫存管理
    url("^CMS/inventory/new_product",views.inventory,name="new_product"),   # 庫存管理
    url("^CMS/inventory/new_inventory",views.inventory,name="new_inventory"),   # 庫存管理
    url("^CMS/material/material_supplier",views.material,name="material_supplier"),   #原料供應商新增
    url("^CMS/material/raw_material",views.material,name="raw_material"),   #原料新增
    url("^CMS/order/",views.order,name="order"), #訂單管理
      
]

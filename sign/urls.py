from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('property_management/',views.prpty_mng,name='property_management'),
    path('amc_mng/',views.amc_mng,name='amc_mng'),
    path('store_mng/',views.store_mng,name='store_mng'),
    path('rem_schedule/',views.rem_schedule,name='rem_schedule'),
    path('vehicle_mng/',views.vehicle_mng,name='vehicle_mng'),
    
    path('build_mnt/',views.build_mnt,name='build_mnt'),
    path('iso_mng/',views.iso_mng,name='iso_mng'),
    path('house_mng/',views.house_mng,name='house_mng'),
    path('purchase_mng/',views.purchase_mng,name='purchase_mng'),
    path('tax_building/',views.tax_building,name='tax_building'),
    path('tenant_mng/',views.tenant_mng,name='tenant_mng'),     

    #path('login',views.login,name='login'),
    #path('forgot_password/',views.forgot_password,name='forgot_password'),
    #path('sign_up/',views.sign_up,name='sign_up'),
    
    #path('', views.login, name='login'),
    path('asset_mng/',views.asset_login,name='asset_login'),
    path('admins/', views.admin_dashboard, name='admin_dashboard'),
    path('viewer/', views.viewer_dashboard, name='viewer_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
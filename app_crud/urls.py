from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('Employee/',views.Employeee, name = "Employee"),
    path('add_emp/',views.add_emp, name = "add_emp"),
    path('update_emp/<int:pk>/', views.update_emp, name='update_emp'),
    path('delete_emp/<int:pk>/', views.delete_emp, name='delete_emp'),
    path('Managerr/', views.Managerr, name='Managerr'),
    path('add_manager/', views.add_manager, name='add_manager'),
    path('update_man/<int:pk>/', views.update_man, name='update_man'),
    path('delete_man/<int:pk>/', views.delete_man, name='delete_man'),
    path('admin/', admin.site.urls),  
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.shp_login, name='shp_login'),
    path('shp_login1/', views.shp_login1, name='shp_login1'),
    path('shp_logout/',views.shp_logout, name='shp_logout'),


    path('shp_home/', views.shp_home, name='shp_home'),

    
    # --------------------------user--------------------
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home, name='user_home'),
    path('services/', views.services, name='services'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointment_success/', views.appointment_success, name='appointment_success'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


]

from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)

urlpatterns = [
    path('',views.shp_login, name='shp_login'),
    path('shp_login1/', views.shp_login1, name='shp_login1'),
    path('shp_logout/',views.shp_logout, name='shp_logout'),


# ------------------------------shop--------------------------------
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    path('shp_home/', views.shp_home, name='shp_home'),
    path('delete_bookings/<int:appointment_id>/', views.delete_bookings, name='delete_bookings'),  # Delete booking


    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='pswd_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='pswd_reset_complete'),

    
    # --------------------------user--------------------
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home, name='user_home'),
    path('services/', views.services, name='services'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('appointment_success/', views.appointment_success, name='appointment_success'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('delete_appointment/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


]

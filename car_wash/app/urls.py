from django.urls import path
from . import views

urlpatterns = [
    path('',views.shp_login, name='shp_login'),
    path('shp_login1/', views.shp_login1, name='shp_login1'),
    path('shp_logout',views.shp_logout),

    
    # --------------------------user--------------------
    path('register/', views.register, name='register'),
    path('user_home/', views.user_home, name='user_home'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]

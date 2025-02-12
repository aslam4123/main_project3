from django.urls import path
from . import views

urlpatterns = [
    path('',views.shp_login, name='shp_login'),

    
    # --------------------------user--------------------
    path('user_home/', views.user_home, name='user_home'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]

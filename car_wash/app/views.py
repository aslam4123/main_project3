from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User

# ---------------------------------Login------------------------------

def shp_login(req):
    if 'car_wash' in req.session:
        return redirect(shp_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['car_wash']=uname   #create session
                return redirect(shp_home)
            else:
                login(req,data)
                req.session['user']=uname   #create session
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(shp_login)
    
    else:
        return render(req,'login.html')


def shp_home(request):
    return render(request, 'user/home.html')




# ---------------------------------user---------------------------------------------
def user_home(request):
    return render(request, 'user/home.html')

# Book Appointment Page
def book_appointment(request):
    return render(request, 'user/book_appointment.html')

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

def shp_login1(req):
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

def shp_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(shp_login)




# ---------------------------------user---------------------------------------------


def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        # send_mail('user registration','eshop account created', settings.EMAIL_HOST_USER, [email])
        try:
           
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shp_login)
        except:
            messages.warning(req,'User already exists.')
            return redirect(register)
    else:
        return render(req,'user/register.html')

def user_home(request):
    return render(request, 'user/home.html')

def services(request):
    # Here we can add data to be passed into the context if necessary for dynamic content
    return render(request, 'user/services.html')  

# Book Appointment Page
from django.shortcuts import render, redirect
from .models import Appointment
from django.http import HttpResponse

def book_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        service = request.POST.get('service')
        date = request.POST.get('date')

        # Create a new appointment
        Appointment.objects.create(
            name=name,
            service=service,
            date=date
        )

        return redirect('appointment_success')  # Redirect to success page or confirmation message

    return render(request, 'user/book_appointment.html')

def appointment_success(request):
    return render(request, 'user/appointment_success.html')

from django.shortcuts import render
from .models import Appointment

def view_appointments(request):
    # Get all appointments from the database
    appointments = Appointment.objects.all().order_by('-date')  # Orders by date, with the most recent first
    return render(request, 'user/view_appointments.html', {'appointments': appointments})


def about(request):
    return render(request, 'user/about.html')


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you can add code to send an email or store the message in the database
        # Example email sending:
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['your_email@example.com'],  # Your email address to receive the form messages
            fail_silently=False,
        )
        return render(request, 'user/contact.html', {'message_sent': True})
    return render(request, 'user/contact.html')


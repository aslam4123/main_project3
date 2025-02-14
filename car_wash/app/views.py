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
    return render(request, 'shop/home.html')

def view_bookings(request):
    # Get all appointments from the database
    appointments = Appointment.objects.all().order_by('-date')  # Orders by date, with the most recent first
    return render(request, 'shop/bookings.html', {'appointments': appointments})

def delete_bookings(request, appointment_id):
    # Fetch the appointment object or return 404 if not found
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Delete the appointment from the database
    if request.method == "POST":
        appointment.delete()
        return redirect('view_bookings')  # 

    # If the request method isn't POST, raise 404 (not allowed here)
    raise Http404("Invalid request method")

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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def book_appointment(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        service = request.POST['service']
        date = request.POST['date']

        # Check if the selected time is already booked
        if Appointment.objects.filter(date=date).exists():
            messages.error(request, 'The selected time slot is already booked. Please choose another time.')
            return redirect('book_appointment')  # Redirect back to the booking form with the error

        # If the time is available, create the appointment
        appointment = Appointment.objects.create(
            user=request.user,  # Associate the appointment with the logged-in user
            name=name, 
            email=email, 
            service=service, 
            date=date
        )
        messages.success(request, 'Your appointment has been booked successfully!')
        return redirect('appointment_success')  # Redirect to appointment success page or another page as required

    return render(request, 'user/book_appointment.html')



def appointment_success(request):
    return render(request, 'user/appointment_success.html')


from django.shortcuts import render
from .models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def view_appointments(request):
    # Get the appointments for the current logged-in user
    appointments = Appointment.objects.filter(user=request.user)

    # Render the template and pass the appointments to it
    return render(request, 'user/view_appointments.html', {'appointments': appointments})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from django.http import Http404

def delete_appointment(request, appointment_id):
    # Fetch the appointment object or return 404 if not found
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Delete the appointment from the database
    if request.method == "POST":
        appointment.delete()
        return redirect('view_appointments')  # Redirect to the appointments page

    # If the request method isn't POST, raise 404 (not allowed here)
    raise Http404("Invalid request method")



def about(request):
    return render(request, 'user/about.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email to admin
            send_mail(
                subject=f"Message from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.ADMIN_EMAIL],
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the contact page or another success page
    else:
        form = ContactForm()

    return render(request, 'user/contact.html', {'form': form})



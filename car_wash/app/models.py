from django.db import models

# Create your models here.
from django.db import models

class Service(models.Model):
    # Define the different types of car wash services
    SERVICE_CHOICES = [
        ('exterior_wash', 'Exterior Wash'),
        ('interior_cleaning', 'Interior Cleaning'),
        ('detailing', 'Car Detailing'),
    ]
    
    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()  # Time duration for service

    def __str__(self):
        return self.name

class Booking(models.Model):
    # Define the fields for booking appointments
    user_name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    notes = models.TextField(blank=True, null=True)  # Additional notes from the user (optional)

    # Define a status for the booking (e.g., pending, confirmed, completed)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking for {self.user_name} - {self.service.name} on {self.appointment_date}"

    class Meta:
        ordering = ['appointment_date']

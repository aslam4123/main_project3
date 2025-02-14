


from django.db import models


from django.contrib.auth.models import User

class Appointment(models.Model):
    # Add a foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    
    # Your other fields like name, email, service, date, etc.
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.service} on {self.date}'


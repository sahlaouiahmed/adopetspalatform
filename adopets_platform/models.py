from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    description = models.TextField()
    photo = models.ImageField(upload_to='static/images/pet_photos/')
    city = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_pets')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-posted_at"]


class AdoptionRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.requester.username} - {self.pet.name}"
    
    class Meta:
        ordering = ["-created_at"]


#__________________________________________#

from django.db import models
from .models import Pet  # or adjust if Pet is in another module

class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='contact_messages')

    def __str__(self):
        return f"{self.sender_name} → {self.pet.name} @ {self.sent_at.strftime('%Y-%m-%d %H:%M')}"

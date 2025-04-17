from django.db import models

# Create your models here.

# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
    
    
class User(AbstractUser):
    # Ajoute tes champs personnalisés ici si besoin
    ROLE_CHOICES = (
        ('stagiaire', 'Stagiaire'),
        ('formateur', 'Formateur'),
        ('admin', 'Administrateur'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    institut = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    payment = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
pass
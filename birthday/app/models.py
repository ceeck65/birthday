from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Guests(models.Model):

    STATUS_CHOICES = (
        ('assist', 'Asistiré'),
        ('not_attend', 'No asistiré'),
        ('maybe', 'Tal vez'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guest')
    title = models.CharField(max_length=200)
    fisrt_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    companions = models.CharField(max_length=200)
    attendance = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='assist')

    
    class Meta:
        verbose_name = 'Invitado'
        verbose_name_plural = 'Invitados'
        ordering = ['-id']


    def __str__(self):
        return self.title

# gestion/models/cliente.py
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

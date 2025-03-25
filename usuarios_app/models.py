from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    ROLES = [
        ('menor', 'Menor afectado por bullying'),
        ('depresion', 'Persona con depresión'),
        ('psicologo', 'Psicólogo / Voluntario'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, default='menor')
    anonimo = models.BooleanField(default=True)  # Para menores que quieran anonimato

    # Evitar colisión con auth.User
    groups = models.ManyToManyField(Group, related_name="usuarios_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuarios_permissions", blank=True)

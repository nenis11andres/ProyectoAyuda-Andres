from django.db import models
from usuarios_app.models import Usuario
from foro_app.models import Publicacion
# Create your models here.
class Chat(models.Model):
    remitente = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='ayudas_enviadas')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='ayudas_recibidas')
    contenido = models.TextField(default="Texto por defecto")
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=True, blank=True, related_name="chats")  # Opcional
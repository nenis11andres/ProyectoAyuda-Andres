from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .models import Comentario
from usuarios_app.models import Usuario
from .forms import PublicacionForm, ComentarioForm

# Create your views here.

def foro(request):
    #Recoger las publicaciones del usuario
    publicaciones=Publicacion.objects.all()
    return render(request, 'foro.html', {'publicaciones': publicaciones})
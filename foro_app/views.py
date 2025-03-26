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

def crear_publicacion(request):
    if request.method == 'POST':
        form=PublicacionForm(request.POST)
        if form.is_valid():
            # Recogemos la publicacion pero no lo guardamos
            publicacion = form.save(commit=False)
            #Asignamos el usuario a la publicacion
            publicacion.autor = request.user
            #Guardamos la publicacion
            publicacion.save()
            #Mostramos de nuevo las publicaciones
            return redirect('foro')
    else:
        form=PublicacionForm()
        
    return render(request, 'nuevapublicacion.html', {'form': form})
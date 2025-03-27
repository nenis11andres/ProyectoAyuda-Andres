from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from usuarios_app.models import Usuario
from .forms import ChatForm
from .models import Chat
from foro_app.models import Publicacion
# Create your views here
def listar_psicologos(request):
    
    usuario_logueado = request.user
    if usuario_logueado.rol == 'psicologo':
        usuarios = Usuario.objects.all()
    else:
        
        usuarios = Usuario.objects.filter(rol='psicologo')
   
    return render(request, 'psicologos.html', {'usuarios': usuarios})

def chat(request, usuario_id):
    receptor = get_object_or_404(Usuario, id=usuario_id)
    remitente = request.user

   
    mensajes = Chat.objects.filter(remitente=remitente, receptor=receptor) | \
              Chat.objects.filter(receptor=remitente, remitente=receptor)

    
    mensajes = mensajes.order_by('id')
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.remitente = remitente
            nuevo_mensaje.receptor = receptor
            nuevo_mensaje.publicacion = None  
            nuevo_mensaje.save()

            
            return redirect('chat', usuario_id=receptor.id)
    else:
        form = ChatForm()

    
    return render(request, "chat2.html", {"form": form, 'mensajes': mensajes})


def chat_foro(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    remitente = request.user

    
    ultimo_psicologo = Chat.objects.filter(publicacion=publicacion, remitente__rol='psicologo').order_by('-id').first()

    
    if remitente == publicacion.autor:
        receptor = ultimo_psicologo.remitente if ultimo_psicologo else None  
    else:
        receptor = publicacion.autor  

    
    if not (remitente == publicacion.autor or remitente.rol == 'psicologo'):
        return redirect('foro')

    # Obtener los mensajes del chat
    mensajes = Chat.objects.filter(publicacion=publicacion)

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid() and receptor:  # Solo guardar si hay receptor válido
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.remitente = remitente
            nuevo_mensaje.receptor = receptor
            nuevo_mensaje.publicacion = publicacion
            nuevo_mensaje.save()
            return redirect('chat_foro', publicacion_id=publicacion.id)
    else:
        form = ChatForm()

    return render(request, "chat.html", {"form": form, "mensajes": mensajes})
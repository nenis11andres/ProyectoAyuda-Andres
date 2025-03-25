from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("foro") # Cambiar esta linea a futuro para la pagina que primero se muestre
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('foro')  # Cambiar esta linea a futuro para la pagina que primero se muestre
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(login_view)


#Provisional
def inicio_view(request):
    return render(request, 'usuarios/inicio.html')
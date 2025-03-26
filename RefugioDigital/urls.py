from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from usuarios_app.views import login_view, registro, logout_view, inicio_view  # eliminar inicio_view cuando se cambie
from foro_app.views import foro

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False), name='root'),  # Redirigir la raíz al login
    path('foro/', foro, name="foro"),
    path('admin/', admin.site.urls),
    path("registro/", registro, name="registro"),
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
]
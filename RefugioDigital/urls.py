"""
URL configuration for RefugioDigital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios_app.views import login_view,registro,logout_view,inicio_view #eliminar inicio_view cuando se cambie
from tests_app.views import index, crear_test, ver_preguntas, agregar_pregunta, eliminar_test, editar_pregunta, eliminar_pregunta

urlpatterns = [
    path('admin/', admin.site.urls),
    path("registro/", registro, name="registro"),
    path("", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('index_tests/', index, name='index_tests'),
    path('crear_test/', crear_test, name='crear_test'),
    path('eliminar_test/<int:pk>', eliminar_test, name='eliminar_test'),
    path('ver_preguntas/<int:pk>', ver_preguntas, name='ver_preguntas'),
    path('agregar_pregunta/<int:pk>', agregar_pregunta, name='agregar_pregunta'),
    path('editar_pregunta/<int:pkPregunta>/<int:pkTest>', editar_pregunta, name='editar_pregunta'),
    path('eliminar_pregunta/<int:pkPregunta>/<int:pkTest>', eliminar_pregunta, name='eliminar_pregunta'),
    
]

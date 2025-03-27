from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from usuarios_app.views import login_view, registro, logout_view, inicio_view
from foro_app.views import foro, crear_publicacion
from tests_app.views import index, crear_test, ver_preguntas, agregar_pregunta, eliminar_test, editar_pregunta, eliminar_pregunta
from chat_app.views import listar_psicologos,chat,chat_foro
urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False), name='root'),  # Redirigir la raíz al login
    path('foro/', foro, name="foro"),
    path('publicacion/nueva', crear_publicacion, name="crear_publicacion"),
    path('admin/', admin.site.urls),
    path("registro/", registro, name="registro"),
    path("login/", login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('index_tests/', index, name='index_tests'),
    path('crear_test/', crear_test, name='crear_test'),
    path('eliminar_test/<int:pk>', eliminar_test, name='eliminar_test'),
    path('ver_preguntas/<int:pk>', ver_preguntas, name='ver_preguntas'),
    path('agregar_pregunta/<int:pk>', agregar_pregunta, name='agregar_pregunta'),
    path('editar_pregunta/<int:pkPregunta>/<int:pkTest>', editar_pregunta, name='editar_pregunta'),
    path('eliminar_pregunta/<int:pkPregunta>/<int:pkTest>', eliminar_pregunta, name='eliminar_pregunta'),
    path('chat/<int:publicacion_id>/',chat_foro,name='chat_foro' ),
    path('chat_psicologo/<int:usuario_id>/',chat,name='chat' ),
    path('listado/', listar_psicologos,name='listar_psicologos')
]
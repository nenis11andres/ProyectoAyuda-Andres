from django.contrib import admin
from .models import Test, Pregunta, Respuesta

# Register your models here.
admin.site.register(Test)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
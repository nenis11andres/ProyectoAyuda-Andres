from django import forms
from .models import Publicacion
from .models import Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields=['contenido'] 
        # No mostramos el campo usuario
        exclude=['fecha', 'comentarios']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['publicacion', 'texto']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'publicacion': forms.HiddenInput(),  # Para no mostrar el campo 'publicacion' en el formulario
        }
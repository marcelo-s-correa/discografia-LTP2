from django import forms
from .models import Musica

class FormMusicas(forms.ModelForm):
    class Meta:
        model = Musica
        fields = [
             'titulo',
             'segundos',
             'album',
            ]

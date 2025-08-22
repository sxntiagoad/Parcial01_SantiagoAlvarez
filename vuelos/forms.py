from django import forms
from .models import Vuelo

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['nombre_vuelo', 'tipo', 'precio']
        widgets = {
            "tipo": forms.Select(),
        }

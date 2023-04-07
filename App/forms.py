from django import forms

class PublicacionForm(forms.Form):
    titulo = forms.TextField(max_length=100)
    precio = forms.CharField(max_length=10)
    descripcion = forms.TextField(max_length=1000)
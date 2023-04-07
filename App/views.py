from django.shortcuts import render

class BuscarPublicacion(ListView):
    model = Publicacion

    def get_queryset(self):
        f = 
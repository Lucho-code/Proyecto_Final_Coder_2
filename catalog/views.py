from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from catalog.models import Libro



from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

class Cargar_libro(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'cargar_libro.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_libro', kwargs={'pk':self.object.pk})
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from faunatrack.models import Projet, Observation
from faunatrack.forms import ProjetForm, ObservationForm

def hello_world(request):
    return render(request, 'base.html')

class ProjetCreate(CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_create.html'
    success_url = reverse_lazy('projet_list')

class ProjetUpdate(UpdateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_update.html'
    success_url = reverse_lazy('projet_list')

class ProjetDelete(DeleteView):
    model = Projet
    template_name = 'projet_confirm_delete.html'
    success_url = reverse_lazy('projet_list')

class ProjetList(ListView):
    model = Projet
    template_name = 'projet_list.html'

class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'observation_create.html'
    success_url = reverse_lazy('projet_list')  # Suppose que l'utilisateur est redirigé vers la liste des projets après l'ajout

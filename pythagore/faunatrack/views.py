from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from faunatrack.models import Projet
from faunatrack.forms import ProjetForm

def hello_world(request):
    return render(request, 'base.html')

class ProjetCreate(CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_create.html'
    success_url = reverse_lazy('projet_list')

class ProjetList(ListView):
    model = Projet
    template_name = 'projet_list.html'

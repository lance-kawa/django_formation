from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from faunatrack.models import Projet, Observation
from faunatrack.forms import ProjetForm, ObservationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def hello_world(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    return redirect('login')

class ProjetCreate(CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_create.html'
    success_url = reverse_lazy('projet_list')

class ProjetUpdate(UserPassesTestMixin, UpdateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_update.html'
    success_url = reverse_lazy('projet_list')

    def test_func(self):
        projet: Projet = self.get_object()
        return self.request.user == projet.responsable.utilisateur

class ProjetDelete(DeleteView):
    model = Projet
    template_name = 'projet_confirm_delete.html'
    success_url = reverse_lazy('projet_list')

class ProjetList(LoginRequiredMixin, ListView):
    model = Projet
    template_name = 'projet_list.html'

class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'observation_create.html'
    success_url = reverse_lazy('projet_list')  # Suppose que l'utilisateur est redirigé vers la liste des projets après l'ajout

    def form_valid(self, form):
        observation = form.save(commit=False)
        # Récupère le projet_id de l'URL
        projet_id = self.kwargs.get('projet_id')
        projet = get_object_or_404(Projet, pk=projet_id)
        # Sauvegarde l'observation
        observation.save()
        # Associe l'observation au projet et sauvegarde
        projet.observations.add(observation)
        # Redirige vers le détail du projet ou une autre URL appropriée
        return redirect('projet_list')
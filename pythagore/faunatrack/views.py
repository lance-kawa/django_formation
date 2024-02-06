from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from faunatrack.models import Projet, Observation, Scientifique
from faunatrack.forms import ProjetForm, ObservationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib import messages


def hello_world(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    return redirect('login')


class AuthorizedMixin(LoginRequiredMixin, PermissionRequiredMixin):
    pass

class ProjetCreate(AuthorizedMixin, CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_create.html'
    success_url = reverse_lazy('projet_list')
    permission_required = "add_projet"

class ProjetUpdate(UserPassesTestMixin, AuthorizedMixin, UpdateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'projet_update.html'
    success_url = reverse_lazy('projet_list')
    permission_required = "change_projet"

    def test_func(self):
        try:
            profil_scientifique = self.request.user.scientifique
            return profil_scientifique and profil_scientifique.observations.all()
        except Scientifique.DoesNotExist:
            return False
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.info(self.request, "You must be logged in to access this page.")
            return super().handle_no_permission()
        else:
            # Custom message for users without a scientifique profile
            messages.error(self.request, "Access denied. You do not have a scientifique profile.", extra_tags="text-red-500")
            # Redirect to a specific URL, e.g., the home page or a profile creation page
            return redirect('home')

class ProjetDelete(DeleteView):
    model = Projet
    template_name = 'projet_confirm_delete.html'
    success_url = reverse_lazy('projet_list')
    permission_required = "delete_projet"


class ProjetList(AuthorizedMixin, ListView):
    model = Projet
    template_name = 'projet_list.html'
    permission_required = "view_projet"

class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'observation_create.html'
    success_url = reverse_lazy('projet_list')  # Suppose que l'utilisateur est redirigé vers la liste des projets après l'ajout
    permission_required = "add_observation"

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
    
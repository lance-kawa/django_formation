from django import forms
from .models import Projet, Observation

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'document', 'responable', 'observations']

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['nom', 'espece', 'latitude', 'longitude', 'date_observation', 'quantite', 'notes']

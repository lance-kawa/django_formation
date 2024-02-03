from django import forms
from django.utils import timezone
from .models import Projet, Observation

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'document', 'responable', 'observations']

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['nom', 'espece', 'latitude', 'longitude', 'date_observation', 'quantite', 'notes']

    def clean_date_observation(self):
        date_observation = self.cleaned_data.get("date_observation")
        if date_observation > timezone.now().date():
            raise forms.ValidationError("La date d'observation ne peut pas être dans le futur.")
        return date_observation
    
    def clean_latitude(self):
        latitude = self.cleaned_data.get("latitude")
        if latitude < -90 or latitude > 90:
            raise forms.ValidationError("La latitude doit être comprise entre -90 et 90.")
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get("longitude")
        if longitude < -180 or longitude > 180:
            raise forms.ValidationError("La longitude doit être comprise entre -180 et 180.")
        return longitude
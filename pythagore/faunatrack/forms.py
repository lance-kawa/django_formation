from django import forms
from django.utils import timezone
from .models import Projet, Observation


class FaunaTrackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FaunaTrackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5'


class ProjetForm(FaunaTrackForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'document', 'responsable']


class ObservationForm(FaunaTrackForm):
    class Meta:
        model = Observation
        fields = ['nom', 'espece', 'latitude', 'longitude', 'date_observation', 'quantite', 'notes']
        widgets = {
            'date_observation': forms.widgets.DateInput( 
                attrs={
                    'type': 'date',
                }
            ),
        }
    quantite = forms.IntegerField(
        label="Quantité",
        help_text="Nombre d'individus observés",
        min_value=1,
        max_value=1000,
    )

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
    
from rest_framework import serializers
from faunatrack.models import Espece

class EspeceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espece
        fields = '__all__'  # Sélectionne tous les champs du modèle

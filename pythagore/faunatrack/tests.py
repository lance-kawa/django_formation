from datetime import datetime
from django.test import TestCase
from django.db.models.signals import post_save
from faunatrack.models import Espece, Observation
from faunatrack.signals import edit_espece_status  # Assurez-vous que le signal est correctement importé
from django.db.models import Sum

class EspeceStatusTest(TestCase):
    def setUp(self):
        # Connectez le signal pour s'assurer qu'il est actif lors du test
        post_save.connect(edit_espece_status, sender=Observation)

        # Créez une espèce pour le test
        self.espece = Espece.objects.create(nom_commun="Lion", nom_scientifique="Panthera leo", status="SAIN")

    def test_espece_status_danger(self):
        # Créez plusieurs observations pour cette espèce avec une quantité totale <= 10
        Observation.objects.create(espece=self.espece, quantite=5, latitude=5, longitude=5, date_observation=datetime.strptime("25/01/2024", "%d/%m/%Y"))
        Observation.objects.create(espece=self.espece, quantite=4, latitude=5, longitude=5, date_observation=datetime.strptime("25/01/2024", "%d/%m/%Y"))

        # Récupérez l'espèce à nouveau pour voir si son statut a été mis à jour
        espece_updated = Espece.objects.get(id=self.espece.id)
        self.assertEqual(espece_updated.status, "DANGER")

    def test_espece_status_sain(self):
        # Créez plusieurs observations pour cette espèce avec une quantité totale > 10 # Total = 13
        Observation.objects.create(espece=self.espece, quantite=7, latitude=5, longitude=5, date_observation=datetime.strptime("25/01/2024", "%d/%m/%Y"))
        Observation.objects.create(espece=self.espece, quantite=5, latitude=5, longitude=5, date_observation=datetime.strptime("25/01/2024", "%d/%m/%Y"))
        Observation.objects.create(espece=self.espece, quantite=1, latitude=5, longitude=5, date_observation=datetime.strptime("25/01/2024", "%d/%m/%Y"))  # Total = 13

        # Récupérez l'espèce à nouveau pour voir si son statut a été mis à jour
        espece_updated = Espece.objects.get(id=self.espece.id)
        self.assertEqual(espece_updated.status, "SAIN")

    def tearDown(self):
        # Déconnectez le signal après le test pour éviter des effets de bord
        post_save.disconnect(edit_espece_status, sender=Observation)

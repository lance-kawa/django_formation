from django.db import models
    
class Espece(models.Model):
    nom_commun = models.CharField(max_length=250, verbose_name="Nom commun")
    def __str__(self):
        return self.nom_commun

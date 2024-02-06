from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify
from faunatrack.validators import validate_latitude, validate_longitude

class Scientifique(models.Model):
    utilisateur = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="profil_scientifique", verbose_name="Utilisateur")
    institution = models.CharField(max_length=250, blank=True, default="CNRS", verbose_name="Institution")

    def __str__(self):
        return self.utilisateur.username
    
class Espece(models.Model):
    nom_commun = models.CharField(max_length=250, verbose_name="Nom commun")
    nom_scientifique = models.CharField(max_length=250, blank=True, default="", verbose_name="Nom scientifique")
    status = models.CharField(choices=[("DANGER", "En danger"), ("SAIN", "Hors de danger")], max_length=250)

    def clean(self):
        if Espece.objects.filter(nom_commun=self.nom_commun).exists():
            raise ValidationError({'nom_commun': "Ce nom d'espèce existe déjà."})

    def __str__(self):
        return self.nom_commun

class Observation(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom")
    espece = models.ForeignKey(Espece, related_name='observations', on_delete=models.CASCADE, verbose_name="Espèce", help_text="Nom de l'espèce observée")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude", validators=[validate_latitude])
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude", validators=[validate_longitude])
    date_observation = models.DateField(verbose_name="Date d'observation")
    quantite = models.IntegerField(verbose_name="Quantité")
    notes = models.TextField(blank=True, default="pas de notes", verbose_name="Notes")
    photos = models.ImageField(upload_to='faunatrack/static/photos_observations/', blank=True, null=True, verbose_name="Photos")

    def __str__(self):
        return f"{self.espece.nom_commun} observée à {self.nom} le {self.date_observation}"

class Projet(models.Model):
    responsable = models.ForeignKey(Scientifique, null=True, blank=True, on_delete=models.SET_NULL, related_name="projet", verbose_name="Responsable")
    titre = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    document = models.FileField(upload_to='faunatrack/static/documents_projets/', blank=True, null=True, verbose_name="Documents")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    observations = models.ManyToManyField(Observation, related_name="projets", verbose_name="Observations")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.titre


    
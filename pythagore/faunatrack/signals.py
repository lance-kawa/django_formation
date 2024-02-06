import datetime
from typing import Union
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum    
from django.contrib.auth.models import Permission
from faunatrack.models import Observation, Scientifique



######################################################################
# Observations
######################################################################

@receiver(post_save, sender=Observation)
def edit_espece_status(sender, instance, created, **kwargs):
    espece = instance.espece
    total_nb_espece = Observation.objects.filter(espece=espece).aggregate(total=Sum("quantite"))["total"]
    if total_nb_espece <= 10:
        espece.status = "DANGER"
    else:
        espece.status = "SAIN"
    espece.save()


@receiver(post_save, sender=Scientifique)
def add_scientifique_permissions(sender, instance, created, **kwargs):
    if created:
        # Récupère toutes les permissions liées à l'application 'faunatrack'
        permissions = Permission.objects.filter(content_type__app_label='faunatrack')
        for permission in permissions:
            instance.utilisateur.user_permissions.add(permission)
        instance.utilisateur.save()

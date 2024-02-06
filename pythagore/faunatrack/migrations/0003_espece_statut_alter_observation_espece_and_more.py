# Generated by Django 5.0.1 on 2024-02-06 09:43

import django.db.models.deletion
import faunatrack.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faunatrack', '0002_espece_nom_scientifique_observation_scientifique_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='espece',
            name='statut',
            field=models.CharField(blank=True, choices=[('DANGER', 'DANGER'), ('SAFE', 'SAFE')], default='SAFE', max_length=250, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='espece',
            field=models.ForeignKey(help_text="Nom de l'espèce observée", on_delete=django.db.models.deletion.CASCADE, related_name='observations', to='faunatrack.espece', verbose_name='Espèce'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, validators=[faunatrack.validators.validate_latitude], verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='observation',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, validators=[faunatrack.validators.validate_longitude], verbose_name='Longitude'),
        ),
    ]
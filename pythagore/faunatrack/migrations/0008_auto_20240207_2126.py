# Generated by Django 5.0.1 on 2024-02-07 21:26

from django.db import migrations
import os

class Migration(migrations.Migration):

    dependencies = [
        ('faunatrack', '0007_projet_slug'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

        try:
            User.objects.get(username=DJANGO_SU_NAME)
        except User.DoesNotExist:
            superuser = User.objects.create_superuser(
                username=DJANGO_SU_NAME,
                email=DJANGO_SU_EMAIL,
                password=DJANGO_SU_PASSWORD)

            superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]

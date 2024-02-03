from django.contrib import admin

from faunatrack.models import Espece, Projet, Scientifique, Observation

# Register your models here.
@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
    pass

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    pass

@admin.register(Scientifique)
class ScientifiqueAdmin(admin.ModelAdmin):
    pass

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

from faunatrack.models import Espece, Projet, Scientifique, Observation
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields


# Ressource pour l'importation
class EspeceImportResource(resources.ModelResource):
    nom = fields.Field(attribute='nom_commun', column_name='nom')
    scient_nom = fields.Field(attribute='nom_scientifique', column_name='scient_nom')

    class Meta:
        model = Espece
        fields = ('id', 'nom', 'scient_nom',)  # Utilisez les noms de champs du modèle
        # Spécifiez 'skip_unchanged = True' pour ignorer les enregistrements inchangés lors de l'importation
        skip_unchanged = True
        # Spécifiez 'report_skipped = False' pour ne pas inclure les lignes ignorées dans le rapport d'importation
        report_skipped = False

# Ressource pour l'exportation
class EspeceExportResource(resources.ModelResource):
    nom_commun = fields.Field(attribute='nom_commun', column_name='Nom Commun')
    nom_scientifique = fields.Field(attribute='nom_scientifique', column_name='Nom Scientifique')

    class Meta:
        model = Espece
        fields = ('id', 'nom_commun', 'nom_scientifique',)
        export_order = ('id', 'nom_commun', 'nom_scientifique',)


class ObservationInlineAdmin(admin.TabularInline):
    model = Observation

@admin.register(Espece)
class EspeceAdmin(ImportExportModelAdmin):
    resource_class = EspeceImportResource
    inlines = [ObservationInlineAdmin]

    def get_import_resource_class(self):
        """
        Retourne la classe de ressource utilisée pour l'importation.
        """
        return EspeceImportResource

    def get_export_resource_class(self):
        """
        Retourne la classe de ressource utilisée pour l'exportation.
        """
        return EspeceExportResource

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    pass

@admin.register(Scientifique)
class ScientifiqueAdmin(admin.ModelAdmin):
    pass

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ["nom", "espece", "date_observation"]
    list_filter = ["espece"]
    search_fields = ["espece__nom_commun"]
    ordering = ["date_observation"]
    list_editable = ["espece"]

    actions = ["marquer_comme_critique"]

    def marquer_comme_critique(self, request, queryset):
        # Boucle sur les observations sélectionnées
        for observation in queryset:
            projets = observation.projets
            for projet in projets.all(): # Assurez-vous que le chemin d'accès à projet est correct
                projet.description = "[CRITIQUE] " + projet.description
                projet.save()
        self.message_user(request, "La description du projet a été mise à jour à 'Critique' pour les observations sélectionnées.")
    marquer_comme_critique.short_description = "Marquer le projet comme Critique"

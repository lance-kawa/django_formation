from django.contrib import admin

from faunatrack.models import Espece

# Register your models here.
@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
    pass

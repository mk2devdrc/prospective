from django.contrib import admin

# Register your models here.
from .models import Categorie, Francais

@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('toUperWorld', 'nom_categorie',)
    ordering = ('nom_categorie',)

    def toUperWorld(self, obj):
        return ("%s"%(obj.nom_categorie)).capitalize()
    toUperWorld.short_description = 'Categorie'


@admin.register(Francais)
class FrancaisAdmin(admin.ModelAdmin):
    list_display = ('toUperWorld', 'titre', 'categorie', 'editeur', 'source', 'date_creation')
    ordering = ('titre',)

    def toUperWorld(self, obj):
        return ("%s"%(obj.titre)).capitalize()
    toUperWorld.short_description = 'Titre'

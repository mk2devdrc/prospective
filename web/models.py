from django.db import models
from django.utils import timezone

# Create your models here.
class Categorie(models.Model):
    """docstring for category."""
    nom_categorie = models.CharField(max_length=40, default='Info Derniere')

    class meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom_categorie

class Francais(models.Model):
    """docstring for Francais"""
    categorie = models.ForeignKey(Categorie, related_name='categorie')
    titre = models.CharField(default='Tire', max_length=90)
    contenu = models.TextField(default='Contenu')
    photo = models.ImageField(upload_to='article_photo/')
    editeur = models.CharField(max_length=50, default='Editeur')
    source = models.CharField(max_length=59, default='Source de la nouvelle')
    date_creation = models.DateField(default=timezone.now)
    date_publication = models.DateField(default=timezone.now)
    date_modification = models.DateField(default=timezone.now)

    class meta:
        verbose_name = 'Francais'
        verbose_name_plural = 'Francais'

    def __str__(self):
        return self.titre

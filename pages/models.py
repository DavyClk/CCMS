# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.urls import reverse  # Add this import
from champs.models import Titre

class Categorie(models.Model):
    titre = models.ForeignKey(Titre, on_delete=models.CASCADE)
    alias = models.SlugField("Alias", max_length=200, unique=True)
    description = models.TextField("Description", blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["titre"]
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        app_label = 'pages'

    def __str__(self):
        return self.titre.titre

    def get_absolute_url(self):
        return reverse("pages_categorie", kwargs={"categorie_alias": self.alias})


class Article(models.Model):
    titre = models.ForeignKey('champs.Titre', on_delete=models.CASCADE)  # or your actual FK definition
    contenu = models.TextField("Contenu", blank=True)
    date_pub = models.DateTimeField(
        "Date de publication", 
        default=datetime.datetime.now
    )
    alias = models.SlugField("Alias", max_length=200, unique=True)
    auteur = models.ForeignKey(
        User, 
        verbose_name="Auteur",
        on_delete=models.CASCADE,
        related_name='articles'
    )
    
    ETAT_CHOICES = (
        (1, "Publié"),
        (2, "Non publié"),
        (3, "Archivé"),
    )
    etat = models.IntegerField("Etat", choices=ETAT_CHOICES, default=1)
    
    categories = models.ForeignKey(
        Categorie,
        verbose_name="Catégorie",
        on_delete=models.CASCADE,
        related_name='articles'
    )

    class Meta:
        ordering = ["-date_pub"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre.titre

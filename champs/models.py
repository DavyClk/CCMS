# -*- coding: utf-8 -*- 

# champs/models.py
from django.db import models

class Titre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)  # Option 1: Make nullabl
    titre = models.CharField("Titre", max_length=200, unique=True)
	#instances = models.PositiveIntegerField("Instances")
	
    class Meta:
        ordering = ['titre']
        app_label = 'champs'  # Explicit app label helps in some cases
        
    def __str__(self):
        return self.titre

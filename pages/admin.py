# -*- coding: utf-8 -*- 

# pages/admin.py

from django.db import models
from django import forms
from django.http import HttpResponseRedirect


from pages.models import Article
from pages.models import Categorie
from champs.models import Titre
from fields.models import TitleField

from pages.forms import CategorieForm
from pages.forms import ArticleForm

from pages.buttons import Button, ButtonAdmin

from django.contrib import admin
from .models import Categorie
from champs.models import Titre

class CategorieAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	form = CategorieForm
	
	buttons = (
		Button('save_one', "Save One"),
		Button('save_all', "Save All"),
		Button('save_some', "Save Some"),
	)
	"""
	def save_model(self, request, obj, form, change):
		print("Save model method")
		obj.save()
	
	def tool_save_one(self, request, obj, button):
		print("Save One method")
		return HttpResponseRedirect('/admin/pages/categorie')
    
	def tool_save_all(self, request, obj, button):
		print("Before : ")
		print(self.form.case)
		
		self.form.case = 2
		
		print("After : ")
		print(self.form.case)
		
		return HttpResponseRedirect('/admin/pages/categorie')
	
	def tool_save_some(self, request, obj, button):
		self.form.case = 3
		return HttpResponseRedirect('/admin/pages/categorie')
	"""  
	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		# Ensure only existing Titres can be selected
		form.base_fields['titre'].queryset = Titre.objects.all()
		return form
	
	
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = { "alias": ("titre",) }
	form = ArticleForm

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)


	

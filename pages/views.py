# -*- coding: utf-8 -*- 

from django.shortcuts import get_object_or_404, render
from pages.models import Categorie, Article
from django.template import RequestContext
from pages.forms import CategorieForm
from champs.models import Titre
from django.http import HttpResponseRedirect
from .models import Categorie  # Make sure to import your model

def categorie_view(request, categorie_alias):
    # Get the category or return 404
    categorie = get_object_or_404(Categorie, alias=categorie_alias)
    
    # Add any additional context you need
    context = {
        'categorie': categorie,
        # Add other context variables here
    }
    
    return render(request, 'pages/categorie.html', context)

def index(request, template_name="pages/index.html"):
    context = {
        'page_title': 'Musical Instruments and Sheet Music for Musicians',
        'cat': Categorie.objects.all(),
    }
    return render(request, template_name, context)

def show_category(request, categorie_alias, template_name="categorie.html"):
	c = get_object_or_404(Categorie, alias=categorie_alias)
	cat = Categorie.objects.all()
	articles = c.article_set.all()
	return render(template_name, locals(),
		context_instance=RequestContext(request))

def show_article(request, article_alias, template_name="article.html"):
	a = get_object_or_404(Article, slug=article_alias)
	cat = Categorie.objects.all()
	categories = a.categorie
	return render(template_name, locals(),
		context_instance=RequestContext(request))

def show_categories(request, template_name="pages/categories.html"):
	page_title = 'Catégories'
	cat = Categorie.objects.all()
	return render(template_name, locals(),
		context_instance=RequestContext(request))

def ajouter_categorie(request, template_name="pages/categorie_add.html"):
	cat = Categorie.objects.all()
	if request.method == 'POST': # If the form has been submitted...
		form = CategorieForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			return HttpResponseRedirect('/categories/') # Redirect after POST
	else:
		form = CategorieForm() # An unbound form

	return render(template_name, locals(),
		context_instance=RequestContext(request))

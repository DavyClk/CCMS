# Generated by Django 5.2.3 on 2025-06-17 01:04

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('champs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.SlugField(max_length=200, unique=True, verbose_name='Alias')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('name', models.CharField(max_length=100)),
                ('titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='champs.titre')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
                'ordering': ['titre'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField(blank=True, verbose_name='Contenu')),
                ('date_pub', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date de publication')),
                ('alias', models.SlugField(max_length=200, unique=True, verbose_name='Alias')),
                ('etat', models.IntegerField(choices=[(1, 'Publié'), (2, 'Non publié'), (3, 'Archivé')], default=1, verbose_name='Etat')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
                ('titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='champs.titre')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='pages.categorie', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date_pub'],
            },
        ),
    ]

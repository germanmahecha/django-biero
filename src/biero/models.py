from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Biere(models.Model):
    nomBiere = models.CharField(max_length=100, blank=False, null=False)
    brasserie = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=256, blank=False, null=False)
    pays = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='bieres/', default='bieres/defaut.jpg')
    ajoute = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifie = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return self.nomBiere

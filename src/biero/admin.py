from django.contrib import admin
from .forms import FormulaireBiere
from .models import Biere # reference au model


@admin.register(Biere)
class AdminBiere(admin.ModelAdmin):
	list_display = ["id","nomBiere", "brasserie","pays","ajoute","modifie"]

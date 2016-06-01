#!/usr/bin/env/ python
# -*-coding:utf-8-*-
from django.http import HttpResponse, HttpResponseRedirect
# Mes importations
from .forms import FormulaireBiere
from .models import Biere
from django.shortcuts import render, get_object_or_404,redirect
from django.template import loader
#authentication des usagers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required



def accueil(request):
	titre = "Accueil"
	bieres = Biere.objects.order_by('-id')
	template = loader.get_template('accueil.html')
	context = {
		"titre" : titre,
		"bieres" : bieres,
	}
	
	return HttpResponse(template.render(context, request))


def details(request, pk):
	titre = "Détails d'une biere"
	biere = get_object_or_404(Biere, pk=pk)
	template = loader.get_template("details.html")
	context = {
		"titre" : titre,
		"biere" : biere,
	}
	
	return HttpResponse(template.render(context, request))

#decorateur
@login_required()
@permission_required('is_superuser')
def ajouter(request):
	titre = "Ajouter une bière"
	if request.method == 'POST':
		form = FormulaireBiere(request.POST, request.FILES)

		if form.is_valid():
			unebiere = form.save(commit=False)
			unebiere.save()
			return HttpResponseRedirect('/')
	else:
		form = FormulaireBiere()

	template = loader.get_template("ajouter.html")
	
	context = {
		"titre" : titre,
		"form" : form
	}
	
	return HttpResponse(template.render(context, request))


def authentication(request):
	titre = "Authentication"
	context = {
		"titre" : titre
		#"form" : form
	}

	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		
		if action == 'connexion':
			user = authenticate(username=username, password=password)
			login(request, user)
		return redirect('/')

	return render(request, "authentication.html", context)



def enregistrement(request):
	titre = "Enregistrement"
	context = {
		"titre" : titre
	}

	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		courriel = request.POST.get('courriel', None)
		password = request.POST.get('password', None)
		
		if action == 'registre':
			user = User.objects.create_user(username=username, email=courriel, password=password)
			user.save()
		return redirect('/authentication')
		
	return render(request, "enregistrement.html", context)


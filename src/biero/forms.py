from django import forms
from .models import Biere
	

class FormulaireBiere(forms.ModelForm):
	class Meta:
		model = Biere
		fields = ["nomBiere","brasserie","description", "pays","image"]

	def clean_nomBiere(self):
		nom = self.cleaned_data.get("nomBiere")
		return nom
	

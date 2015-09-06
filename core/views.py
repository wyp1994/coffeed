from django.shortcuts import render
from django.views.generic import TemplateView #Drag in HTML
# Create your views here.

class SplashView(TemplateView):
	template_name = "index.html"


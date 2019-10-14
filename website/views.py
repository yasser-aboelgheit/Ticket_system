from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class HomePageView(TemplateView):
    template_name = 'website/home.html'
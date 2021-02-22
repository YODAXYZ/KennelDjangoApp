from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from pet.models import Animal


# class IndexPageView(TemplateView):
#     template_name = 'index.html'


class ContactsView(TemplateView):
    template_name = 'contact.html'


class AboutUsVies(TemplateView):
    template_name = 'about-us.html'


class PetListView(ListView):
    template_name = 'pets/pet-list.html'
    model = Animal


class PetView(DetailView):
    template_name = 'pets/pet-deteil.html'
    model = Animal




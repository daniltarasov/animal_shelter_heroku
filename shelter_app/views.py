from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from shelter_app.models import Animal


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    # template_name = "base/base.html"

class AnimalChoice(TemplateView):
    template_name = "animal_choice.html"

class AnimalList(ListView):
    model = Animal
    template_name = 'animals.html'
    context_object_name = "animals"

    def get_queryset(self):
        type_of_animal = self.request.GET['type']
        # type_of_animal = "собака"
        return Animal.objects.filter(animal_type__type=type_of_animal)

class AnimalView(DetailView):
    model = Animal
    template_name = 'animal_view.html'

class ContactPageView(TemplateView):
    template_name = "contacts.html"

from django.contrib import admin
from shelter_app.models import AnimalType, Animal

# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    @staticmethod
    def type_of_animal(obj):
        return obj.animal_type.type

    list_display = ('name', 'type_of_animal', 'breed')
    fields = ('animal_type', 'breed', 'name', 'sex', 'age', 'color', 'castrated', 'vaccinated', 'photo', 'description')


@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    pass



     
     
     
     
    
     
     
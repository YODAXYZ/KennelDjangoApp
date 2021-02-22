from django.contrib import admin
from pet.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass
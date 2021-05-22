from django.contrib import admin
from .models import MyCustomUser
from food.models import Food,FoodEnergy

admin.site.register(MyCustomUser)
admin.site.register(Food)
admin.site.register(FoodEnergy)
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import FoodSerializer
from .models import FoodEnergy,Food
@login_required(login_url='login')
def home(request):
    food_url=Food.objects.filter(name='Гематоген').values()[0]
    print(food_url)
    return render(request,'food/food-list.html',context={"food_url":food_url})

@login_required(login_url='login')
def test(request):
    return render(request,'food/test.html')


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


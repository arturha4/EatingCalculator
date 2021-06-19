from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response

from .serializers import FoodSerializer,FoodEnergySerializer
from .models import FoodEnergy,Food
@login_required(login_url='login')
def home(request):
    food_url=Food.objects.filter(name='Гематоген').values()[0]
    print(food_url)
    return render(request,'food/food-list.html',context={"food_url":food_url})

@login_required(login_url='login')
def test(request):
    return render(request,'food/test.html')
@login_required(login_url='login')
def foodview(request):
    return render(request,'food/foodview.html')


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer




class FoodEnergyViewSet(viewsets.ModelViewSet):
    queryset = FoodEnergy.objects.all()
    serializer_class = FoodEnergySerializer


    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(**kwargs)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)




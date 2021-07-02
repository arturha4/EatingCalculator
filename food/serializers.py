from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import Food,FoodEnergy


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'


class FoodEnergySerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodEnergy
        fields='__all__'




    def validate(self, attrs):
        namea=attrs.get('name')
        if FoodEnergy.objects.filter(name=namea).exists():
            raise serializers.ValidationError(f'This FoodEnergy object called: {namea}, is exist')
        return attrs


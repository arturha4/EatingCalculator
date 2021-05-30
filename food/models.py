from django.db import models

class FoodEnergy(models.Model):
    name=models.TextField(max_length=100)
    kilocalories=models.IntegerField()
    carbohydrates=models.FloatField()
    fats=models.FloatField()
    proteins=models.FloatField()
    def __str__(self):
        return self.name



class Food(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.TextField(max_length=100)
    image=models.ImageField(upload_to='static/images')
    energy=models.OneToOneField(FoodEnergy,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


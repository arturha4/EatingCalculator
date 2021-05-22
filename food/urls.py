from django.urls import path, include
from accounts import views
from food import views as foodviews


urlpatterns = [
    path('',views.home_page,name='home'),
    path('/food-list',foodviews.home,name='food')
]
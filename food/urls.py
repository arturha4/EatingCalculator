from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import views
from food import views as foodviews


urlpatterns = [
    path('',views.home_page,name='home'),
    path('/food-list',foodviews.home,name='food'),
    path('/test',foodviews.test,name='')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
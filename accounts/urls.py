from django.urls import path
from . import views
from accounts.views import CustomLoginView

urlpatterns=[
    path('login',CustomLoginView.as_view(),name='login'),
    path('home',views.home_page,name='home'),
    path('registration',views.RegistrationView.as_view(),name='register'),
    path('logout',views.userlogout,name='logout')
]
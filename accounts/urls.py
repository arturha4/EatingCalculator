from django.urls import path, include
from . import views
from accounts.views import CustomLoginView

urlpatterns=[
    path('login',CustomLoginView.as_view(),name='login'),
    path('registration',views.RegistrationView.as_view(),name='register'),
    path('logout',views.userlogout,name='logout')
]
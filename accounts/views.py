from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from django.contrib import messages
from django.contrib.auth import authenticate

from accounts.forms import NewUserForm, UserLoginForm
from accounts.models import MyCustomUser


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
    form_class =UserLoginForm
    def post(self, request, *args, **kwargs):
        print(request.POST)
        usrname = request.POST['username']
        passwrd = request.POST['password']
        user = authenticate(request, username=usrname, password=passwrd)
        if user is not None:
            return redirect('/home')
        messages.error(request, "Пользователя с такими данными не сущетсвует")
        return redirect('/login')


class RegistrationView(FormView):
    template_name = "accounts/register.html"
    success_url = "/login"
    form_class = NewUserForm

    def post(self, request, *args, **kwargs):
        data=request.POST
        email=data['email']
        password=data['password']
        first_name=data['first_name']
        second_name=data['second_name']
        MyCustomUser.objects.create_user(email,password,first_name,second_name)
        messages.info(request,f'Добро пожаловать: {first_name} {second_name}')
        return redirect('/login')



def home_page(request):
    return render(request, 'accounts/home.html')


from django.shortcuts import render

# Create your views here.

import django
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from accounts.forms import NewUserForm, UserLoginForm
from accounts.models import MyCustomUser


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
    form_class =UserLoginForm
    def post(self, request, *args, **kwargs):
        print(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.info(request, f'Добро пожаловать: {username}')
            return redirect('/home/food')
        messages.error(request, "Пользователя с такими данными не существует")
        return redirect('/login')

    def get(self,request,*args,**kwargs):
        myform=UserLoginForm
        return render(request,'accounts/login.html',{'form':UserLoginForm})

class RegistrationView(FormView):
    template_name = "accounts/register.html"
    success_url = "/login"
    form_class = NewUserForm

    def post(self, request, *args, **kwargs):
        try:
            data=request.POST
            email=data['email']
            password=data['password']
            first_name=data['first_name']
            second_name=data['second_name']
            MyCustomUser.objects.create_user(email, password, first_name, second_name)
            return redirect('/login')
        except  django.db.utils.IntegrityError:
            messages.info(request,'Пользователь с такой почтой уже существует')
            return redirect('/registration')





@login_required(login_url='login')
def home_page(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render

# Create your views here.

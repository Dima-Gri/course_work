from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

import user
from .forms import *
from .models import *

menu = [
    {'title': 'Регистрация', 'url_name': 'register'},
    {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'user/form.html', context=context)


def reg(request):
    return render(request, 'user/register.html')


def login(request):
    return render(request, 'user/login.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name=form.cleaned_data['group'])
            user.groups.add(user_group)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})







class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_success_url(self):
        user_name = self.request.POST['username']
        user_group = CustomUser.objects.filter(username=user_name)
        print(user_group[0].group)
        if user_group[0].group == 'Менеджер':
            return reverse_lazy('manager_panel')
        else:
            return reverse_lazy('user_panel')


def logout_user(request):
    logout(request)
    return redirect('login')


def move_to_user_panel(request):
    return render(request, 'user/login_user.html')


def move_to_manager_panel(request):
    return render(request, 'user/login_admin.html')




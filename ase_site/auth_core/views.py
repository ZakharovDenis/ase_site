from django.conf.urls import url, include
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import RedirectView

from .forms import UserLoginForm, UserForm
from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect(r"/")
    else:
        if request.method == "POST":
            try:
                nxt = request.GET['next']
            except:
                nxt = ""
            one = request.POST.get("Login")
            two = request.POST.get("Password")
            user = authenticate(email=one, password=two)
            if user is not None:
                if user.is_active == 0:
                    userform = UserLoginForm()
                    return render(request, "ase_site/auth_core/templates/login_form.html",
                                  {"form": userform, 'values': ['Дождитесь активации']})
                else:
                    login(request, user)
                    if nxt != "":
                        return redirect(nxt)
                    else:
                        return redirect('/')
            else:
                userform = UserLoginForm()
                return render(request, "ase_site/auth_core/templates/login_form.html",
                              {"form": userform, 'values': ['Неверный логин или пароль']})
        else:
            userform = UserLoginForm()
            return render(request, "ase_site/auth_core/templates/login_form.html", {"form": userform})


def logout_view(request):
    logout(request)
    return redirect("/")


def register_view(request):
    args = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "ase_site/auth_core/templates/wait.html")
    else:
        form = UserForm()
    args['form'] = form
    return render(request, "ase_site/auth_core/templates/register_form.html", args)

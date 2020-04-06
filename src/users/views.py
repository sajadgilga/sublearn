from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def user_home(request):
    context = {
            "title": "User home",
            }
    return render(request, 'home/index.html', context=context)

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect("users:login")
    else:
        form = UserCreationForm()

    context = {
            "title": "User register",
            "form": form
            }
    return render(request, 'home/register.html', context=context)

def user_login(request):
    context = {
            "title": "User Login",
            }
    return render(request, 'home/index.html', context=context)

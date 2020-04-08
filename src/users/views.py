from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserUpdateForm, ProfileUpdateForm


# Create your views here.

def user_home(request):
    context = {
            "title": "User home",
            }
    return render(request, 'users/home.html', context=context)

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
    return render(request, 'users/register.html', context=context)

@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("users:profile")

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', context={
        'u_form': u_form,
        'p_form': p_form,
        })

def user_index(request):
    return render(request, 'index.html')


from django.shortcuts import render


# Create your views here.

def user_test(request):
    return render(request, 'home/index.html', context={})
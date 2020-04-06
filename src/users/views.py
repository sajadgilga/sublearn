from django.shortcuts import render


# Create your views here.

def user_home(request):
    context = {
            "title": "Kiarash",
            }
    return render(request, 'home/index.html', context=context)



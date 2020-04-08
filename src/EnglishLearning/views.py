from django.shortcuts import render, redirect

"""
Don't add any functions in this app except the index page
"""

def index(request):
#    return render(request, 'index.html')
    return redirect('users:home')

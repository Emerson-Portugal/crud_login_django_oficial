
#app.login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def home(request):
    return render(request, 'blog/index.html')

def exit(request):
    logout(request)
    return redirect('/')


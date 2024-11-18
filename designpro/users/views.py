from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            return render(request, 'users/login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('core:home')

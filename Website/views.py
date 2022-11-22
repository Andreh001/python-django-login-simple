from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
def signin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('Panel')
        else:    
            return render(request, 'login.html')
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
        else:
            login(request, usuario)
            return redirect('Panel')

@login_required
def panel(request):
    return render(request, 'panel.html')

@login_required
def signut(request):
    logout(request)
    return redirect('Login')
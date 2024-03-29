from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from catalog.models import Administrativo, Usuario

from .forms import User_registration_form

#VISTA INICIO
def index(request):
    return render(request, 'index.html')

#VISTA USUARIO
def usuario(request):
    return render(request, "catalog/registrarse.html")

#VISTA ADMINISTRATIVO
def administrativos(request):
    
    return render(request, 'catalog/administrativos.html')

def administrativos(request):
    
    if request.method == "POST":
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']
        print(request.POST)
        Administrativo.objects.create(usuario=usuario,contrasena=contrasena)
        return render(request, 'catalog/inicio.html')
    
    return render(request, 'catalog/administrativos.html')

#VISTA REGISTRO
def registrarse(request):

    return render(request, 'catalog/registrarse.html')

def registrarse(request):
    
    if request.method == "POST":
       usuario = request.POST['usuario']
       contrasena = request.POST['contrasena']
       email = request.POST['email']
       direccion = request.POST['direccion']
       departamento = request.POST['departamento']
       print(request.POST)
       Usuario.objects.create(usuario=usuario,contrasena=contrasena,email=email,direccion=direccion,departamento=departamento)
       return render(request, 'catalog/inicio.html')
    return render(request, 'catalog/registrarse.html')

#VISTA CONTACTO
def contacto(request):
        return render(request, 'catalog/contacto.html')









def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)

def logout_view(request):
    logout(request)
    return redirect('index')



def about(request):
    return render(request, 'about.html')

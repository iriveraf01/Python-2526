from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# Vista de la página de inicio de la tienda
def index(request):
    return render(request, 'shop/index.html')

def registro(request):
    if request.method == 'POST':
        # Aquí procesaríamos el formulario de registro
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'shop/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def iniciar_sesion(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Usuario o contraseña incorrectos. Revisa tus piezas."
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form, 'error_messages': error_message})
# en Startapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import LoginForm, UserUpdateForm
from .models import CustomUser  # Asegúrate de importar CustomUser desde tu aplicación

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Cambia 'inicio' por tu vista de inicio
        else:
            # Handle invalid login
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('inicio')  # Cambia 'inicio' por tu vista de inicio
    return render(request, 'logout.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia 'login' por tu vista de login
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class NotLoginView(FormView):
    template_name = 'not_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Handle invalid login
            messages.error(self.request, "Usuario o contraseña incorrectos.")
            return self.form_invalid(form)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

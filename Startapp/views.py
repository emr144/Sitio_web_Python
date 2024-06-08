from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.generic import FormView
from .forms import LoginForm
from django.urls import reverse_lazy


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Cambia 'inicio' por tu vista de inicio
    else:
        form = AuthenticationForm()
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




class not_login_view(FormView):
    template_name = 'not_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        # Autenticar al usuario
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensaje de error
        messages.error(self.request, "Debes iniciar sesión para acceder a esta página.")
        return super().form_invalid(form)

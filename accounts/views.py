from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Кастомный класс для входа
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль.')
        return super().form_invalid(form)

# Кастомный класс для выхода
class CustomLogoutView(LogoutView):
    next_page = 'index'
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы успешно вышли из системы.')
        return super().dispatch(request, *args, **kwargs)

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
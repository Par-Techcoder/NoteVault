from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from notes.models import User


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirem_password = request.POST.get('confirm_password')
        if password == confirem_password:
            if User.objects.filter(email=email).exists():
                return render(redirect, 'login')
            # Create a new user
            user = User.objects.create_user(username=email, password=password)
            user.save()
            login(request, user)
            return redirect('home')
        

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')            
        else:
            return render(redirect, 'register')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

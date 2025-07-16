from django.views import View
from django.shortcuts import render, redirect
from notes.models import User
from django.contrib.auth import authenticate, login, logout
from passlib.hash import bcrypt


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')        

        if password != confirm_password:
            return render(request, 'auth/register.html', {
                'error': "Passwords do not match."
            })

        if User.objects(email=email).first():
            return redirect('login')  # Redirect to login if user exists

        hashed_password = bcrypt.hash(password)

        user = User(email=email, password=hashed_password)
        user.save()

        return redirect('login')  # Redirect to login after successful registration


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects(email=email).first()

        if user and bcrypt.verify(password, user.password):
            # Simulate login by storing user ID in session
            request.session['user_id'] = str(user.id)
            return redirect('note_list')  # Replace with your notes page
        else:
            return render(request, 'auth/login.html', {
                'error': 'Invalid credentials. Please try again or register.'
            })
        


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

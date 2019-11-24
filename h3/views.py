from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        # form = User
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request, self.template_name)

class LogoutView(View):
    # template_name = 'login.html'

    def get(self, request):
        logout(request)
        return redirect('/login')

class SignupView(View):
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        return render(request, 'signup.html', context={'form': form})

    def get(self,request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
        

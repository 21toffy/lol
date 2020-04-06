# Project level views

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import(
    authenticate,
    login,
    logout
)
from todo.forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

class LandingView(View):
    def get(self,request):
        # this displays the landing page
        template_name  = 'landing/landing.html'
        context = {}
        return render(request,template_name,context)

#login logic
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('notes:home'))
            else:

                return HttpResponseRedirect(reverse('login'))
                messages.error(request, 'this account is not active')
        else:
            messages.error(request, 'Bad username or password')

    return render (request, 'login.html', {})


#register logic
def register_view(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, password=password, email=email)
            messages.success(request, 'Thanks for registering {}'.format(user.username))
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form':form})




#logout logic

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
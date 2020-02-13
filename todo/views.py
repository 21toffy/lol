from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import Note_form
import datetime
from django.contrib import messages 
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserRegisterForm


@login_required
def home(request, username):
    current_user = request.user
    username=current_user.username
    note = Note.objects.filter(owner=current_user)
    if request.method == 'POST':
        form = Note_form(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = current_user
            new_note.date = datetime.datetime.now()
            new_note.save()
            return Redirect('notes:home', kwargs={'username':username})

    else:
        form=Note_form()
    context = {'current_user':current_user, 'note':note, 'form':form}    
    return render(request,'dashboard.html',context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return Redirect('notes:home', kwargs={'username':username})
            else:
                
                return Redirect('notes:login')
                messages.error(request, 'this account is not active')
        else:
            messages.error(request, 'Bad username or password')

    return render (request, 'login.html', {})


def register_view(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, password=password, email=email)
            messages.success(request, 'Thanks for registering {}'.format(user.username))
            return Redirect('notes:login')
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form':form})




def logout_view(request):
    logout(request)
    return Redirect('login')


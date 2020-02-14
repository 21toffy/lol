from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import Note_form, edit_note_form
import datetime
from django.http import HttpResponseRedirect
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
    current_user = request.user #for the url, in other to pick the current user
    username=current_user.username #for the url, in other to pick the current users username
    note = Note.objects.filter(owner=current_user)#to get the notes of only the current user
    #the add note form
    if request.method == 'POST':
        form = Note_form(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = current_user
            new_note.date = datetime.datetime.now()
            new_note.save()
            return HttpResponseRedirect(reverse('notes:home', kwargs={'username':username}))

    else:
        form=Note_form()
    context = {'current_user':current_user, 'note':note, 'form':form}    
    return render(request,'dashboard.html',context)



#login logic
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('notes:home', kwargs={'username':username}))
            else:
                
                return HttpResponseRedirect(reverse('notes:login'))
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
            return HttpResponseRedirect(reverse('notes:login'))
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form':form})




#logout logic

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def note_detail(request, slug, pk):
    note = get_object_or_404(Note, pk=pk, slug=slug)
    current_user = request.user #for the url, in other to pick the current user
    username=current_user.username #for the url, in other to pick the current users username
    context = {'note':note, 'username':username}
    # return HttpResponseRedirect(reverse('note_detail', kwargs={'username':username, 'id':id}))
    return render(request, 'note_detail.html', context)
    

def edit_note(request, pk, slug):
    note = get_object_or_404(Note, pk=pk, slug=slug)
    if request.user != note.owner:
        return redirect('notes:home')

    if request.method=="POST":
        form =edit_note_form(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'note edited succesfully')
    else:
        form = edit_note_form(instance=note)
    return render(request, 'edit_note.html', {'note':note, 'form':form})
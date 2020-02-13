from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import Note_form
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse




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
            return HttpResponseRedirect(reverse('notes:home', kwargs={'username':username}))

    else:
        form=Note_form()
    context = {'current_user':current_user, 'note':note, 'form':form}    
    return render(request,'dashboard.html',context)
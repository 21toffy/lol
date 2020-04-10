from django.shortcuts import render, get_object_or_404,redirect
# from django.contrib.auth.models import User
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import Note_form, edit_note_form
import datetime
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.contrib.auth import(
#     authenticate,
#     get_user_model,
#     login,
#     logout
# )






@login_required
def home(request):
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
            messages.success(request, '{} added'.format(new_note.title))
            return HttpResponseRedirect(reverse('notes:home', kwargs={'username':username}))

    else:
        form=Note_form()
    context = {'current_user':current_user, 'note':note, 'form':form}
    return render(request,'dashboard.html',context)

@login_required
def note_detail(request, slug, pk):
    note = get_object_or_404(Note, pk=pk, slug=slug)
    current_user = request.user #for the url, in other to pick the current user
    username=current_user.username #for the url, in other to pick the current users username
    context = {'note':note, 'username':username}
    # return HttpResponseRedirect(reverse('note_detail', kwargs={'username':username, 'id':id}))
    return render(request, 'note_detail.html', context)

#edit  Note  function
def edit_note(request, pk, slug):
    note = get_object_or_404(Note, pk=pk, slug=slug)
    if request.user != note.owner:
        return redirect('login')

    if request.method=="POST":
        form =edit_note_form(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'note edited succesfully')
    else:
        form = edit_note_form(instance=note)
    return render(request, 'edit_note.html', {'note':note, 'form':form})

##delete note function
def delete_note(request, slug, pk):
    note = get_object_or_404(Note, pk=pk, slug=slug)
    current_user = request.user #for the url, in other to pick the current user
    username=current_user.username #for the url, in other to pick the current users username
    if request.user != note.owner:
        return redirect('login')
    if request.method=='POST':
        note.delete()
        messages.success(request, 'note has been deleted', extra_tags='alert alert-success alert-dismissible fade show')
        return redirect('notes:home')
    return render(request, 'note_confirm_delete.html', {'note':note})


from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Todo, Status
from django.contrib.auth.decorators import login_required



@login_required
def home(request, username):
    user = User.objects.get(username=username)
    todo = Todo.objects.all()
    status = Status.objects.all()
    context{'status':status, 'todo':todo}    
    return render(request,'user_courses_list.html',context)
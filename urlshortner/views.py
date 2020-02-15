from django.shortcuts import render,redirect,get_object_or_404
from .models import Link
from django.views import View
from .forms import CreateLinkForm
# Create your views here.


class CreateShortenedLink(View):
  form = CreateLinkForm()
  def get(self,request):
    #get link and sortened link
    form = CreateLinkForm()
    template_name = ''
    context = {'create_form':form}
    return render(request,template_name,context)

  def post(self,request):
    # post link to generate shortened link
    template_name = ''
    context = {}
    return render(request,template_name,context)



class RedirectLink(View):
  def get(self,request,attach=None):
    # redirect to the url
    attach_phrase = str(attach)
    link = get_object_or_404(Link, attach = attach_phrase)
    redirect_link  = link.url
    return redirect(redirect_link)

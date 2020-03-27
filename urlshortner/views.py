from django.shortcuts import render,redirect,get_object_or_404
from .models import Link
from django.views import View
from .forms import CreateLinkForm
# Create your views here.
from django.contrib import messages


class CreateShortenedLink(View):
  def get(self,request):
    #get link and sortened link
    form = CreateLinkForm()
    template_name = 'create_url.html'
    context = {'form':form}
    return render(request,template_name,context)

  def post(self,request):
    form = CreateLinkForm(request.POST)
    # post link to generate shortened link
    if form.is_valid():
        niickname = form.cleaned_data['niickname']
        url = form.cleaned_data['url']
        link = Link.objects.create(niickname=niickname, url=url)
        messages.success(request, 'Your url has been shortened and can be accessed via  http://127.0.0.1:8000/{}'.format(link.attach))
        return redirect('urlshortner:shortner')




class RedirectLink(View):
  def get(self,request,attach=None):
    # i should add a try nd except catchto handle errors here
    # redirect to the url
    attach_phrase = str(attach)
    link = get_object_or_404(Link, attach = attach_phrase)
    redirect_link  = link.url
    return redirect(redirect_link)

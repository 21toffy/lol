from django.contrib import admin
from django.urls import path,include
from .views import CreateShortenedLink,RedirectLink
app_name  = 'urlshortner'

urlpatterns = [
    path('', CreateShortenedLink.as_view() , name='shortner'),
    path('<str:attach>/', RedirectLink.as_view()),
]

from django.urls import path

from .views import home
app_name = 'notes'

urlpatterns = [
    path('<str:username>/', home, name='home' ),
]
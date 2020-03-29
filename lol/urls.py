from django.contrib import admin
from django.urls import path,include
from todo.views import login_view,logout_view,register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlshortner.urls',namespace='urlshortner')),
    path('notes', include('todo.urls',namespace='notes')),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/register/', register_view, name='register'),
]

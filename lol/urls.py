from django.contrib import admin
from django.urls import path,include
from lol import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingView.as_view() , name='landing' ),
    path('notes/', include('todo.urls',namespace='notes')),
    path('urlshortner', include('urlshortner.urls',namespace='urlshortner')),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
]

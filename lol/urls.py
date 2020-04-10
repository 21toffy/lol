from django.contrib import admin
from django.urls import path,include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('todo.urls', namespace='notes')),
=======
from lol import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingView.as_view() , name='landing' ),
    path('notes/', include('todo.urls',namespace='notes')),
    path('urlshortner', include('urlshortner.urls',namespace='urlshortner')),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
>>>>>>> develop
]

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('todo.urls', namespace='notes')),
]

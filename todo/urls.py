from django.urls import path
from . import views
from .views import home, login_view, register_view, logout_view, note_detail, edit_note, delete_note, LandingView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'notes'

urlpatterns = [

    #home page and dashboard
    path('', LandingView.as_view() , name='landing' ),
    path('notes/mine/', home, name='home' ),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('<slug:slug>/<int:pk>/', note_detail, name='note_detail'),
    path('edit/note/<slug:slug>/<int:pk>', edit_note, name='edit_note'),
    path('delete/note/<slug:slug>/<int:pk>', delete_note, name='note_confirm_delete'),


    
]
if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

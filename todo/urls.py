from django.urls import path

from .views import home, login_view, register_view, logout_view, note_detail, edit_note
app_name = 'notes'

urlpatterns = [
    path('<str:username>/', home, name='home' ),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view),
    path('accounts/register/', register_view, name='register'),
    path('<slug:slug>/<int:pk>/', note_detail, name='note_detail'),
    path('edit/<slug:slug>/<int:pk>', edit_note, name='edit_note')
]
from django.urls import path

from .views import home, login_view, register_view, logout_view, note_detail, edit_note, delete_note
app_name = 'notes'

urlpatterns = [

    #home page and dashboard
    path('<str:username>/', home, name='home' ),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('<slug:slug>/<int:pk>/', note_detail, name='note_detail'),
    path('edit/note/<slug:slug>/<int:pk>', edit_note, name='edit_note'),
    path('delete/note/<slug:slug>/<int:pk>', delete_note, name='note_confirm_delete'),
]
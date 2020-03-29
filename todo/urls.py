from django.urls import path,include

from .views import home, login_view, register_view, logout_view, note_detail, edit_note, delete_note, LandingView

app_name = 'notes'

urlpatterns = [

    #home page and dashboard
    path('home', LandingView.as_view() , name='landing' ),
    path('mine/', home, name='home' ),
    path('<slug:slug>/<int:pk>/', note_detail, name='note_detail'),
    path('<slug:slug>/<int:pk>/edit', edit_note, name='edit_note'),
    path('<slug:slug>/<int:pk>/delete', delete_note, name='note_confirm_delete'),

]
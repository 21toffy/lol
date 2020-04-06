from django.urls import path,include
from todo import views

app_name = 'notes'

urlpatterns = [

    #home page and dashboard
    path('', views.home, name='home' ),
    path('<slug:slug>/<int:pk>/', include([
        path('',views.note_detail, name='note_detail'),
        path('edit', views.edit_note, name='edit_note'),
        path('delete', views.delete_note, name='note_confirm_delete')
        ])),
]
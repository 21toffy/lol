from django import forms
from .models import Note




class Note_form(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','note']

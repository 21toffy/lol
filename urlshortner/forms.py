from django import forms
from .models import Link

class CreateLinkForm(forms.ModelForm):
  # ...
  class Meta:
    model =Link
    fields = ('niickname','url')
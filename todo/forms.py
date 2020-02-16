from django import forms
from .models import Note
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import(
    authenticate,
    get_user_model
)




class Note_form(forms.ModelForm):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class':'form-control'}))

    note = forms.CharField(label='note', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Note
        fields = ['title','note']


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'})

    )
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    # def clean_password1(self):
    #     password = self.cleaned_data['password']
    #     password2 = self.cleaned_data['password2']

    #     if password != password2:
    #         raise ValidationError('passwords dont match!!')
    #     return password2


    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get("password2")
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('passwords do not match')

    def clean_email(self):
        email = self.cleaned_data['email']
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise ValidationError('This email has already been regitered')
        return email


class edit_note_form(forms.ModelForm):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class':'form-control'}))

    note = forms.CharField(label='note', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Note
        fields = ['title','note']

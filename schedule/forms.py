from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs = {'class': 'form-control', 'placeholder': 'Primeiro nome'}
        self.fields['lastname'].widget.attrs = {'class': 'form-control', 'placeholder': 'Sobrenome'}
        self.fields['phone'].widget.attrs = {'class': 'form-control', 'placeholder': 'Número do celular'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'E-Mail'}
        self.fields['description'].widget.attrs = {'class': 'form-control', 'placeholder': 'Descrição'}
        self.fields['show'].widget = forms.NullBooleanSelect(attrs={'class': 'form-control', 'placeholder': 'Exibir'})
        self.fields['picture'].widget.attrs = {'class': 'form-control', 'placeholder': 'Foto'}
        self.fields['category'].widget.attrs = {'class': 'form-control', 'placeholder': 'Categoria'}

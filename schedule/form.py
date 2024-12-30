from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        labels = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ...
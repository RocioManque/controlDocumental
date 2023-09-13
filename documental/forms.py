from django import forms
from .models import documento

class documentoform(forms.ModelForm):
    class Meta:
        model = documento
        fields ='__all__'
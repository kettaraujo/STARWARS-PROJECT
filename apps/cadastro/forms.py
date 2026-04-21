from django import forms
from .models import Jedi


class JediForm(forms.ModelForm):
    class Meta:
        model = Jedi
        fields = '__all__'
from django import forms
from main.models import model_short

class form_long(forms.ModelForm):
    class Meta:
        model = model_short
        fields = ['long_url']
from django import forms
from forms.models import user
class name(forms.ModelForm):
   class Meta:
     model = user
     fields = '__all__'


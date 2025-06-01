from django import forms
from .models import student

class  addmodel(forms.ModelForm):
    class Meta:
      model = student
      fields =["name", "subject", "location"]
      
        
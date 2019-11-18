from django import forms
from . import models

class sosform(forms.ModelForm):
    class Meta:   
        model = models.sos 
        fields = ("latitude","longitude","name","phone")


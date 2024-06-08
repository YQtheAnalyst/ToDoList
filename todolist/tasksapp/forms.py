from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'})) something is wrong

    class Meta:
        model = task # what model are we trying to create the form
        fields = '__all__'


from dataclasses import fields
from django.forms import ModelForm
from .models import Task

class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','memo','important']
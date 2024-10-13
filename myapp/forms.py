from django import forms
from .models import Project, Task


class CreateNewProject(forms.Form):
    name = forms.CharField(label='Título del Proyecto', max_length=300, widget=forms.TextInput(attrs={'class':'input'}))


class CreateNewTask(forms.Form):
    title = forms.CharField(label='Título de tarea', max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(
        label='Descripción de la tarea',
        widget=forms.Textarea(attrs={'class':'input'}),
        required=False
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        label='Proyecto'
    )

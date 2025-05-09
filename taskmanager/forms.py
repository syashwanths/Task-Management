from django import forms
from taskmanager.models import TASK

class TaskForm(forms.ModelForm):
    class Meta:
        model = TASK
        fields = "__all__"

class EditTaskForm(forms.ModelForm):
    task_id = forms.CharField(disabled=True)
    assigned_by = forms.CharField(disabled=True)
    class Meta:
        model = TASK
        fields = ['task_id','task_name','assigned_by','description','assigned_to','priority','status']


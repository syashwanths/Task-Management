from django.contrib import admin
from taskmanager.models import TASK,TaskImage

# Register your models here.
admin.site.register(TASK)
admin.site.register(TaskImage)
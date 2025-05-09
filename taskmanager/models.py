from django.db import models

# Create your models here.
class TASK(models.Model):
    state = [
        ('completed','Completed'),
        ('not completed','Not Completed')
    ]
    task_id = models.CharField(max_length=20)
    task_name = models.CharField(max_length=100)
    assigned_by = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    description = models.TextField()
    assigned_date = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=state)

    def __str__(self):
        return self.task_name
    
class TaskImage(models.Model):
    var = models.ForeignKey(TASK,related_name='tasks',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='userimg',blank=True,null=True)

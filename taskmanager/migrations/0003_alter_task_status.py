# Generated by Django 4.2.17 on 2025-01-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('not completed', 'Not Completed')], max_length=20),
        ),
    ]

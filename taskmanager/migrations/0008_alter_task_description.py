# Generated by Django 4.2.17 on 2025-01-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0007_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
    ]

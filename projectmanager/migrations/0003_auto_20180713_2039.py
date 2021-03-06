# Generated by Django 2.0.7 on 2018-07-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0002_auto_20180707_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_managers',
            field=models.ManyToManyField(blank=True, related_name='project_manager', through='projectmanager.ProjectManager', to='projectmanager.Employee'),
        ),
        migrations.AlterField(
            model_name='project',
            name='resources',
            field=models.ManyToManyField(blank=True, related_name='project_resource', through='projectmanager.ProjectResource', to='projectmanager.Employee'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0021_auto_20180825_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Due Date'),
        ),
    ]

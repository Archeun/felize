# Generated by Django 2.0.7 on 2018-08-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0007_workentry_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workentry',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]

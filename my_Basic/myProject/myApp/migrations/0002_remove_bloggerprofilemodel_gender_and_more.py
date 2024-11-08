# Generated by Django 5.1 on 2024-11-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloggerprofilemodel',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='viewersprofilemodel',
            name='Gender',
        ),
        migrations.AddField(
            model_name='custom_user',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100, null=True),
        ),
    ]

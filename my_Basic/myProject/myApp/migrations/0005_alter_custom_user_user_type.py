# Generated by Django 5.1 on 2024-11-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_bloggerprofilemodel_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='user_type',
            field=models.CharField(choices=[('viewers', 'Viewers'), ('bloogger', 'Bloogger')], max_length=100, null=True),
        ),
    ]

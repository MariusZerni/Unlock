# Generated by Django 3.0.5 on 2020-04-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20200422_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprofile',
            name='fullDescription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

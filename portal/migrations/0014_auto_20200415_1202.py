# Generated by Django 3.0.5 on 2020-04-15 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20200415_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorrelationship',
            name='from_mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_mentor', to='portal.Client'),
        ),
        migrations.AlterField(
            model_name='mentorrelationship',
            name='to_mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_mentee', to='portal.Client'),
        ),
    ]
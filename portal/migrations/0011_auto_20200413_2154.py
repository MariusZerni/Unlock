# Generated by Django 3.0.5 on 2020-04-13 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20200413_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorrelationship',
            name='from_mentor',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='from_mentor', to='portal.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorrelationship',
            name='to_mentee',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='to_mentee', to='portal.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='mentorRelationship',
            field=models.ManyToManyField(through='portal.MentorRelationship', to='portal.User'),
        ),
        migrations.AlterUniqueTogether(
            name='mentorrelationship',
            unique_together={('from_mentor', 'to_mentee')},
        ),
        migrations.RemoveField(
            model_name='mentorrelationship',
            name='mentee',
        ),
        migrations.RemoveField(
            model_name='mentorrelationship',
            name='mentor',
        ),
    ]
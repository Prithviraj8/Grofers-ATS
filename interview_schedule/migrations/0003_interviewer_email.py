# Generated by Django 3.1.6 on 2021-03-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_schedule', '0002_auto_20210306_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]

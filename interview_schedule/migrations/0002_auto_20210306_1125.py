# Generated by Django 3.1.6 on 2021-03-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='interviewer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='interviewer_candidate',
        ),
    ]

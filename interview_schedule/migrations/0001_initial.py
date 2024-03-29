# Generated by Django 3.1.6 on 2021-03-06 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='interviewer_candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_stage', models.CharField(max_length=50)),
                ('interview_schedule_time', models.CharField(max_length=100)),
                ('interviewer_feedback', models.CharField(max_length=100)),
                ('interviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.recruiter')),
            ],
        ),
    ]

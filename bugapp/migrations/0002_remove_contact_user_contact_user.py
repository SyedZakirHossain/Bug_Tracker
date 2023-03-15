# Generated by Django 4.1.5 on 2023-01-10 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugapp.team'),
        ),
    ]

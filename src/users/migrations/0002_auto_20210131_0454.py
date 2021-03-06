# Generated by Django 3.1.5 on 2021-01-31 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='User',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=15),
        ),
    ]

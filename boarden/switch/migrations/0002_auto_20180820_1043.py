# Generated by Django 2.1 on 2018-08-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabulary',
            name='definition',
        ),
        migrations.RemoveField(
            model_name='vocabulary',
            name='example',
        ),
    ]

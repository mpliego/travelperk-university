# Generated by Django 2.1.15 on 2020-05-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together={('name', 'recipe')},
        ),
    ]
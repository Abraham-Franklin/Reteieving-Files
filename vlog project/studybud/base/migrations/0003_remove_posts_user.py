# Generated by Django 4.1.7 on 2023-05-04 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_posts_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
    ]

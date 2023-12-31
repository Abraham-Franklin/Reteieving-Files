# Generated by Django 4.1.7 on 2023-05-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('images_post', models.ImageField(upload_to='images/')),
                ('category', models.CharField(choices=[('Anime', 'Anime'), ('Entertainment', 'Entertainment'), ('Sports', 'Sports'), ('Tech', 'Tech')], max_length=50)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

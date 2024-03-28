# Generated by Django 5.0.1 on 2024-03-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=150)),
                ('topic', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

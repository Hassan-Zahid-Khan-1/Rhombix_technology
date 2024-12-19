# Generated by Django 5.1.3 on 2024-11-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=800)),
                ('link', models.URLField()),
            ],
        ),
    ]

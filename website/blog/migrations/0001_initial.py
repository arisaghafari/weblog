# Generated by Django 3.1.1 on 2020-09-06 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('publish', models.DateTimeField(default=datetime.datetime(2020, 9, 6, 9, 19, 58, 866950, tzinfo=utc))),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1)),
            ],
        ),
    ]

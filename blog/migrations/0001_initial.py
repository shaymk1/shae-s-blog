# Generated by Django 5.0.3 on 2024-03-07 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('image', models.ImageField(blank=True, default='img/placeholder.svg', null=True, upload_to='articles')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Category', models.CharField(max_length=250)),
                ('sub_title', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('time_required_to_read', models.CharField(default='2 Min Read', max_length=250)),
                ('is_admin', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-date_created',),
            },
        ),
    ]

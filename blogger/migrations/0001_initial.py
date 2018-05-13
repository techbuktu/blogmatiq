# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 20:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('page', models.SlugField(blank=True, max_length=110, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=350, verbose_name='Description')),
                ('page', models.SlugField(blank=True, max_length=120)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blogger.Blog')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=500)),
                ('page', models.SlugField(blank=True, max_length=100)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blogger', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('page', models.SlugField(blank=True, max_length=120)),
                ('body', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blogger.BlogCategory')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blogger.Blogger'),
        ),
    ]

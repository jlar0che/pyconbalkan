# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('event', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.PositiveIntegerField()),
                ('number', models.PositiveIntegerField()),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('max_attendees', models.PositiveIntegerField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(0, 'International'), (1, 'National')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('count_down', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

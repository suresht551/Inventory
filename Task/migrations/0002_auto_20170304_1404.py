# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-04 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='C:\\Users\\haris\\Documents\\EmployeeManagemnt\\MyApp\\static\\images'),
        ),
    ]
# Generated by Django 5.1.1 on 2024-10-02 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='cat',
        ),
        migrations.AddField(
            model_name='cat',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='cat.breed'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='ratings',
            field=models.ManyToManyField(related_name='cats', to='cat.rating'),
        ),
    ]

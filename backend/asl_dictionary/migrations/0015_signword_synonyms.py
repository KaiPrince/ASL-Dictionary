# Generated by Django 3.0.5 on 2020-04-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asl_dictionary', '0014_auto_20200423_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='signword',
            name='synonyms',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

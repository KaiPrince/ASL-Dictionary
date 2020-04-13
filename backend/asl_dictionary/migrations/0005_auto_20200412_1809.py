# Generated by Django 3.0.5 on 2020-04-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asl_dictionary', '0004_auto_20200410_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signword',
            name='images',
            field=models.ManyToManyField(blank=True, to='asl_dictionary.SignImage'),
        ),
        migrations.AlterField(
            model_name='signword',
            name='videos',
            field=models.ManyToManyField(blank=True, to='asl_dictionary.SignVideo'),
        ),
    ]